<?php
  class Solr {
    var $base_url;
    var $request;
    var $action;
    var $q;
    var $filter_queries;
    var $sort;
    var $results_per_page;

    var $response;
    var $qtime;
    var $num_found;
    var $start;
    var $page_count;
    var $lower;
    var $upper;
    function Solr($base_url) {
      $this->base_url = $base_url;
      $this->request = $_REQUEST;   // For now, use the HTTP request parameters to build a Solr query
      $this->action = $params['qt'];
      if (!$this->action) { $this->action = "browse"; }
      $this->q = $this->request['q'];
      $this->filter_queries = $this->request['fq'];
      // Build URL to query Solr
      $url = $base_url."/".$this->action."?q=".urlencode($this->q)."&wt=phps";
      $this->start = $this->request['start'];
      $this->sort = $this->request['sort'];
      if ($this->sort) {
        $url .= "&sort=".urlencode($this->sort);
      }
      if ($this->start) {
        $url .= "&start=$this->start";
      }
      if (is_array($this->filter_queries)) {
        $url .= "&fq=".join("&fq=",$this->filter_queries);
      }
      if (!$this->filter_queries && !$this->q) {
        // No filters or query, set rows = 0 so we only display facets
        $url .= "&rows=0";
      }
      // Query Solr
      $unserializedResult = file_get_contents($url);
      $this->response = unserialize($unserializedResult);
      // Process Solr response
      $params = $this->response['responseHeader']['params'];
      $this->qtime = $this->response['responseHeader']['QTime'];
      $this->sort = $params['sort'];   // sort gets overridden from the response parameters, in case it was empty
      $this->results_per_page = $params['rows'];
      if(!$this->results_per_page) {$this->results_per_page=10;}
      $this->num_found = $this->response['response']['numFound'];
      $this->start = $this->response['response']['start'];
      $this->page_count = ceil($this->num_found / $this->results_per_page);
      $this->lower = $this->start + 1;
      $this->upper = $this->start + $this->results_per_page; // || $this->num_found
      if ($this->upper > $this->num_found) {$this->upper = $this->num_found;}
      $this->page_number = $this->start / $this->results_per_page;
      if ($this->page_count > 0) {$this->page_number = $this->page_number + 1;}
    }
    function url_for_search_action($action,$query,$filter_queries,$sort,$start) {
      $url = "browse.php?q=".urlencode($query);
      if ($sort) {
        $url .= "&sort=".urlencode($sort);
      }
      if ($start) {
        $url .= "&start=$start";
      }
      if (is_array($filter_queries)) {
        $url .= "&fq[]=".join("&fq[]=",$filter_queries);
      }
      $url .= "&action=".$action;
      return $url;
    }
    function url_for_search($query,$filter_queries,$sort,$start) {
      return $this->url_for_search_action($this->action,$query,$filter_queries,$sort,$start);
    }
    function url_for_sort($sort) {
      //   #macro(url_for_sort $sort $params)#url_for_search($params.q,$request.getParameterValues('fq'),$sort,0,$params)#end
      return $this->url_for_search($this->q, $this->filter_queries, $sort, 0);
    }
    function url_for_mlt($id) {
      // #macro(url_for_mlt $id, $params)#url_for_search_action("mlt","id:$esc.html($solr.queryEscape($id))",[],$params.sort,0)#end
      // TODO: query parser escape id
      return $this->url_for_search_action('mlt',"id:$id",nil,$this->sort,0);
    }
    function url_for_page($page) {
      //   #macro(url_for_page $page $params)#url_for_search($params.q,$request.getParameterValues('fq'),$params.sort,$pageInfo.startForPage($page),$params)#end
      return $this->url_for_search($this->q, $this->filter_queries, $this->sort, ($page - 1) * $this->results_per_page);
    }
    function url_for_additional_facet($query) {
      //   #macro(url_for_additional_facet $query $params)#url_for_search($params.q,$request.getParameterValues('fq'),$params.sort,0,$params)&fq=$esc.url($query)#end
      return $this->url_for_search($this->q,$this->filter_queries,$this->sort,0)."&fq[]=$query";  // TODO: URL encode $query
    }
    function url_for_single_facet($query) {
      //   #macro(url_for_single_facet $query $params)#url_for_search($params.q,[$query],$params.sort,0,$params)#end
      return $this->url_for_search($this->q,array($query),$this->sort,0);
    }
    function url_for_no_facets() {
      //   #macro(url_for_no_facets $params)#url_for_search($params.q,[],$params.sort,0,$params)#end
      return $this->url_for_search($this->q,nil,$this->sort,0);
    }
  }
  $solr = new Solr("http://localhost:8983/solr/docs");
?>

<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN">
<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title>Solr PHP Example</title>
    <link type="text/css" rev="StyleSheet" rel="StyleSheet" href="main.css"/>
  </head>
  <body>
    <div id="header">
      <div id="logo"><a href="browse.php"><img border="0" src="li_logo_blue-small.jpg" alt="Lucid logo"></a></div>
    </div>
    <div class="main">
	  <div class="search">
        <form action="browse.php" type="get">
          <div id="query">
            <span class="bold">Query</span>: <input type="text" name="q" value="<%=htmlspecialchars($solr->q)%>" size="32"> <span class="submit"><input type="submit" value="Search"></span>
          </div>
        </form>
        <% if(is_array($solr->filter_queries)) { %>
          <div id="filters">
            <span class="bold">Filters</span>:
            <% foreach($solr->filter_queries as $fq) { %>
              <a href="<%=$solr->url_for_single_facet($fq)%>"><%=$fq%></a>
            <% } %>
            <a href="<%=$solr->url_for_no_facets()%>">clear filters</a>
          </div>
        <% } %>
      </div>

      <div id="buffer">
        <span id="search-results-meta">
	      Results <%=$solr->lower%> - <%=$solr->upper%> of <%=$solr->num_found%> for <span class="bold"><%=htmlspecialchars($solr->q)%></span> (<%=$solr->qtime%> milliseconds)
        </span>
      </div>

      <div id="sort-results">
        <span>
	      <span class="bold">Sort By (desc)</span>: <% if(!stristr($solr->sort,'score')) { %><a href="<%=$solr->url_for_sort("score desc")%>">Relevance</a><% } else { %>Relevance<% }%>
	                                                <% if(!stristr($solr->sort,'timestamp')) { %><a href="<%=$solr->url_for_sort("timestamp desc")%>">Date</a><% } else { %>Date<% }%>
	                                                <% if(!stristr($solr->sort,'random')) { %><a href="<%=$solr->url_for_sort("random1 desc")%>">Random</a><% } else { %>Random<% }%>
	    </span>
      </div>

      <% if ($solr->response['facet_counts']['facet_fields']) {%>
        <div id="facets">
          <% foreach ($solr->response['facet_counts']['facet_fields'] as $field => $values) { %>
            <div id="field-facets">
              <div>
                <span class="facet-field"><%=$field%></span>
                <% foreach($values as $value => $count) { %>
                  <div>
	                <a href="<%=$solr->url_for_additional_facet("$field:$value")%>"><%=$value%></a> (<%=$count%>)
                  </div>
                <% } %>
              </div>
            </div>
          <% } %>
        </div>
      <% } // if facets %>

<%var_dump($solr->response['response'])%>

      <% if ($solr->response['response']['docs']) {%>
	      <div id="search-results">
	        <% foreach($solr->response['response']['docs'] as $doc) { %>
	          <div class="search-result-item">
	            <table>
	              <% foreach($doc as $field => $value) { %>
	                <tr>
	                  <td><%=$field%>:</td>
	                  <td>
	                    <% if(is_array($value)) {
	                        print(htmlspecialchars(join(",",$value)));
	                      } else {
	                        print(htmlspecialchars($value));
	                      }
	                    %>
	                  </td>
	                </tr>
	              <% } %>
	            </table>
	          </div>
	        <% } %>
	      </div>
	  <% } %>

      <div id="sort-results">
        <span>
	      <span class="bold">Sort By (desc)</span>: <% if(!stristr($solr->sort,'score')) { %><a href="<%=$solr->url_for_sort("score desc")%>">Relevance</a><% } else { %>Relevance<% }%>
	                                                <% if(!stristr($solr->sort,'timestamp')) { %><a href="<%=$solr->url_for_sort("timestamp desc")%>">Date</a><% } else { %>Date<% }%>
	                                                <% if(!stristr($solr->sort,'random')) { %><a href="<%=$solr->url_for_sort("random1 desc")%>">Random</a><% } else { %>Random<% }%>
	    </span>
      </div>

      <div id="paging">
        <span class="bold">Page</span>:
          <% if($solr->page_number > 1) { %>
            <a class="prev-page" href="<%=$solr->url_for_page($solr->page_number - 1)%>">Previous</a>
          <% } %>

          <% if($solr->page_number > 1) {
	           $page_lower = $solr->page_number - 9;
	           if ($page_lower < 1) {$page_lower = 1;}
	           for ($page_num = $page_lower; $page_num < $solr->page_number; $page_num += 1) { %>
		           <a class="page" href="<%=$solr->url_for_page($page_num)%>"><%=$page_num%></a>
          <%   }
             } %>
          <span class="page-num"><%=$solr->page_number%></span>

          <% $page_upper = $solr->page_number + 9;
             if ($page_upper > $solr->page_count) {$page_upper = $solr->page_count; }
             for ($page_num = $solr->page_number + 1; $page_num <= $page_upper; $page_num += 1) {%>
	           <a class="page" href="<%=$solr->url_for_page($page_num)%>"><%=$page_num%></a>
	      <% } %>
          <% if($solr->page_number < $solr->page_count) { %>
            <a class="next-page" href="<%=$solr->url_for_page($solr->page_number + 1)%>">Next</a>
          <% } %>
      </div>


      <div class="searchBottom">
        <form action="browse.php" type="post">
          <div id="query">
            <span class="bold">Query</span>: <input type="text" name="q" value="<%=htmlspecialchars($q)%>" size="32"> <span class="submit"><input type="submit" value="Search"></span>
          </div>
        </form>
      </div>

	</div>
    <div id="footer">
      <div>© <a href="http://www.lucidworks.com">Lucidworks</a>.</div>
    </div>
  </body>
</html>
