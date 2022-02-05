<html><head><meta charset="UTF-8"/>
  		<meta name="description" content="Black Hole Search"/>
  		<meta name="keywords" content="A multi-language & machine learning capable Solr index searching solution that can fit in your pocket."/>
  		<meta name="author" content="diveyez@r2nhosting.com"/>
  		<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
			<link rel="stylesheet" type="text/css" href="style.css"/><link rel="stylesheet" type="text/css" href="nav.css"/><link rel="stylesheet" type="text/css" href="sidebar.css"/>
      <link href="http://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
      <title>Black Hole Search - Notebooks, Libraries, AI, and Technology in one place.</title>
      </head>
<!-- ADD SECURITY HEADERS ASAP FOR PUBLIC LIBRARY -->

<!-- TOP CONTENT -->
  <div id="cont">
        <!-- RESPONSIVE NAV BAR --> <center>
        <div class="topnav" id="myTopnav">
          <a href="index.php" class="active">Home</a>
          <a href="about.php">About</a>
          <a href="news.php">News</a>
          <a href="search.php">Search</a>
          <a href="queries.php">Queries Explained</a>
          <div class="dropdown">
            <button class="dropbtn">Explore
              <i class="fa fa-caret-down"></i>

            </button>
            <div class="dropdown-content">
              <a href="https://github.com/diveyez/blackhole">Contact Developer</a>
            </div>
          </div>
          <a href="#"></a>
          <a href="javascript:void(0);" style="font-size:15px;" class="icon" onclick="myFunction()">&#9776;</a>
        </div>
        <script>
        function myFunction() {
            var x = document.getElementById("myTopnav");
            if (x.className === "topnav") {
                x.className += " responsive";
            } else {
                x.className = "topnav";
            }
        }
        </script></center><body>
        <!--RESPONSIVE NAV BAR -->
			<a href="./"><img src="images/blackhole.png" height="125" width="190"></img></a></br>
<!-- TOP CONTENT -->
<center></center>

<!-- MAIN CONTENT (SEARCH TOOLTIPS)-->
<div class="tooltip">
<span class="tooltiptext">Library: 'library'</b> </br> Server: localhost</span>
								<form method="post" action="search.php"/>
                <p><b>Keywords:</b><input name="search" type="text" />
                <b>Library:</b><input name="library" type="text" />
                <b>Server:</b><input name="server" type="text" />
                <input class="button1" name="submit" type="submit" value="Search The Galaxy"/></p></form></div>
<!-- MAIN CONTENT (SEARCH ARRAY CODE)-->
                <div id="ww">
			<?php
				if($_POST['search']) { echo "</br>Search Successful, here are the results."; }
					else { echo ("</br><h1>You did not search! Try again!</h1>"); }
								$query = $_POST['search']; $library = $_POST['library']; $server = $_POST['server'];
								echo "</br>"; // Gonna need more fancy shit here to wow them
		 						$starttime = microtime(true); $endtime = microtime(true); printf("Search performed in %f seconds", $endtime - $starttime );
								$ch = curl_init(); $encode = urlencode($query); $encode1 = urlencode($library); $encode2 = urlencode($server);
								curl_setopt($ch,CURLOPT_URL,"http://".$encode2.":8983/solr/".$encode1."/select?q=".$encode."&hl.q=".$encode."&wt=php&indent=true&fl=id,name,score&group=true&group.field=content&hl=on&hl.fl=*&hl.encoder=html&hl.fragmenter=regex&hl.regex.slop=1.0&hl.fl=text_*&hl.usePhraseHighlighter=true&hl.bs.type=WHOLE&hl.defaultSummary=true&hl.offsetSource=POSTINGS&hl.fragsize=125000&hl.maxAnalyzedChars=25000&hl.highlightMultiTerm=true&hl.tag.pre=<b>&hl.tag.post=</b>&results=50");
                curl_setopt($ch, CURLOPT_HEADER, false);                                                                         // fl=content removed to avoid debug clutter              //   //
								curl_setopt ($ch, CURLOPT_RETURNTRANSFER, true); $re = curl_exec($ch); curl_close($ch); $arr;
								eval("\$arr = " . $re . ";"); echo "<p><b>You searched for:</b><i>" . $query . "</i>"; echo "</br>";
								echo "<b>Found:</b><i>" . $arr['response']['numFound'] . "</i> results\n and displaying max 50.</p>" ;
								echo "<ptext><b>Found Matching Text/Terms:</b></ptext></br>";
								foreach($arr['response']['docs'] as $text) { echo "<div id='ww2'><pcontent><b>Found:</b></br><b>" . $text['id'] . "</b></br>" .$text['content'] . "</br>" . "\n</pcontent></div></br></br>"; } //echo implode(',', $arr), "\n";// ?>
</br></div></div>

</body></html>
