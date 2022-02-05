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
          <a href="queries.php">Queries Explained</a>
          <a href="search.php">Search</a>
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
			<a href="./"><center><img src="images/blackhole.png" height="125" width="190"></img></a></br></center>
<!-- TOP CONTENT -->

<center>
                <div class="tooltip">
    						<span class="tooltiptext">Libraries:"This is whatever you called the core during setup. ie: 'library' "</b> </br> Server: localhost</span>
              <form method="post" action="search.php">
              <searchbox><b>Keywords:</b><input name="search" type="text" /><b>Library:</b>
              <input name="library" type="text" /><b>Server:</b><input name="server" type="text" /></searchbox>
              <input class="button1" name="submit" type="submit" value="Search The Galaxy"/></p></form></div></br>

<!-- CONTENT REGION -->
              <div id="pqueries">
              <h3>This is the cheat sheet to utilizing my web to index technology.</h3>
              <h4>Here you can find commonly uncommon queries for searches.</h4>
              <div id="pqueries">
              If you wish to find something specific, you can type any  "phraseyouwish" </br>
              Doing so like that, should allow you to locate more specific results.</br></pqueries>
              </br>
              <h4>Lets start simple, a Forced search.</h4>
              <div id="pqueries">
              Forced searching is as simple as it sounds, just add a plus sign, and experiment.  "adam +laverne" </br>
              Many other engines automatically exclude "where", "how", "and", etc. They call them stop words. We are not implementing stop words in the same way.</br>
              Instead we will use it to our advantage to improve results across the board. Add a plus sign and watch the positivity flow.</br>
              </pqueries>
              </br>
              <h4>Next we will talk about ranges. As you know, it dont take much to count to 100.</h4>
              <div id="pqueries">
              So how can we do that in a search? I am a fan of cryptocurrencies,</br>
              Lets try this, "bitcoin $6000..$80000"</br>
              A simple change like that, makes all the difference and can increase the speed of research drastically.</br>
              </pqueries>
              </br>
              <h4>Let do one more simple search query then move to more advanced techniques.</h4>
              <div id="pqueries">
              This one is simple, I just want to find my long lost friend Billy from High School.</br>
              My searches will obviously be formatted in the following ways.</br>
              First name (or first initial), last name, city (state is optional)</br>
              First name (or first initial), last name, state</br>
              First name (or first initial), last name, area code</br>
              First name (or first initial), last name, zip code</br>
              Phone number, including area code</br>
              Last name, city, state</br>
              Last name, zip code</br>
              Simple right? Well, lets take a closer look at this. There is a set field structure to this.</br>
              You can swap the fields with anything you want and get combination searches with amazing results.</br>
              Now that you know the basics, lets try some more advanced stuff.</br>
              </pqueries>
              </br>
              <div id="pqueries"><h5>Wildcards & What?</h5>
              Two Unique but similar tricks also incorporated are highlighting and wildcards.</br>
              So if I the developer wanted to look through 50,000 pdf's and extract one specific word,</br>
              Perhaps a middle name I do not know,</br>
              I would type the following into the search box  "'MICHAEL'*'DOUGLAS'"  .</br>
              If you want to highlight something for the search so it returns better results</br>
              You would use something like this:  "Something I Need To Find&hl.q=Something More Specific From That Document, Site, Etc. -*" </br>
              In that search query what I did was term in, highlight something better, than subtract all the wildcard and extra bulk output.</br>
              </pqueries>
              </br>
                <h4>That is too much information, lets take it back a step.</h4>
                <div id="pqueries">
              Okay, Wildcards produce too many results. How do we avoid that?</br>
              We will search with the following  "'-MICHAEL'*'-DOUGLAS'" </br>
              This will strip the first and last name, but still match results to</br>
              Any results that match the pre and post phrase to minimize results.</br></pqueries>
              </br>
                <h4>What if I need to find more than one thing?</h4>
                <div id="pqueries">
              Lets say, we just indexed a website, or a book, into the library for searching.</br>
              What now? How do I limit my results to one <b>specific title</b> or <b>site/dir</b> ?</br>
              Think of the : as your saviour. What we want to do now, is type</br>
              the following:  "Website.com:phrase/sentence" "booktitle:phrase/sentence" </br>
              How about matching activity with that?  "website1.com site:website2.com" </br>
              This same principle can be applied to documents as well.</br></pqueries>
              </br>
                <h4>Doing that, for the documents, is fun, and tricky.</h4>
                <div id="pqueries">
              What we need to do now is explain things a bit more.</br>
              The way this works is it catalogs information in arrays in a database.</br>
              This is how it is able to match things together and give results.</br></br>
              </br><b>Hypothetical Situation:</b>  I am sick, I have been sick for a while.</br>
              I have been to the doctor and ..... It is time to find the cure myself.</br>
              Very common in todays world, people are data mining for solutions without realizing it.</br>
              This is how we are going to do this, I will type  "Medicine book:'Antibiotics'-*" </br>
              The results output 3 of 2,357 books, one of which is "Curing a Bacterial Infection at Home"</br>
              Another situation is looking for a specific date. Lets have a history lesson.</br></pqueries></br></br></br>
              <div id="historybox"><p2 style="font-size:14px;">
              The Birthday of the Supreme Court  'September 26th' . The Judiciary Act of 1789 is passed by Congress and signed by  President George Washington , </br>
              establishing the  Supreme Court of the United States</b> as a tribunal made up of six justices who were to serve on the court until death or retirement. </br>
              That day,  President Washington  nominated John Jay to preside as chief justice, and  John Rutledge, William Cushing, John Blair, Robert Harrison, </br>
              and James Wilson  to be associate justices. </br>
              On   September 26</b>,  all six appointments were confirmed by the U.S. Senate.</br>
               The U.S. Supreme Court</b> was established by   Article 3 of the U.S. Constitution</b>.  </br>
              The Constitution granted the  Supreme Court</b> ultimate jurisdiction over all laws, especially those in which their constitutionality was at issue. </br>
              The high court was also designated to oversee cases concerning treaties of the  United States</b>, foreign diplomats, admiralty practice, and maritime jurisdiction. </br>
              On  February 1, 1790 , the first session of the  U.S. Supreme Court</b> was held in  New York City’s Royal Exchange Building .</br>
              </p2></div></br></br>
              <div id="pqueries">
              So I will search for a historical moment,  "DAY:DATE Monday:February 1, MONTH:YEAR '1790'&hl.q=sumreme court&-*" </br>
                </pqueries>
                <h4>Vice Versa</h4>
                <div id="pqueries">
              How do things actually weigh against each other?</br>
              Let's try that,  "Alcohol vs. Wine" </br>
              Simple, what it does is weights them against one another and produces a competitive result.</br>
              Competition in results are always a good thing with computers. I adore this method and strongly recommend it.</br>
                </pqueries>
              </br>
              <h4>Defining Your Search, Refining The Result</h4>
              <div id="pqueries">
              How do we do that? The title of this section is plain and simple.</br>
              In order to do this, we do one simple thing,  "DEFINE: 'whats on your mind'". </br>
              As you learn to mix these techniques you can come up with cool stuff like this:</br>
               "How To book:'DEFINE: Home Made Solar Panels'-*" </br>
              We will use the example from the prevoius section and improve upon it next.</br>
               "DEFINE:DAY:DATE Monday:February 1, MONTH:YEAR '1790'&hl.q=sumreme court&-*"</br>
              </pqueries>
              </br></br>
              <h4>Now that you have learned this, master it, because it will help you refine your search and get better results, even on other engines.</h4>
              <div id="pqueries">This was built for my personal Library. However I was asked to provide it for others so I am taking it all the way. </br>
                I hope you enjoy the work that is to come! Happy Searching!</pqueries></br><!-- FOOTER AREA -->
              </div></center>
</br></br></br></br></br></br></br>
</div>
<!-- FOOTER AREA -->
						<div id="footer"><center>
								<h5> <a href="https://github.com/diveyez/blackhole/">Black Hole</a> by <a href="https://github.com/diveyez/">Ricky 'Diveyez' N.</a></p>&copy; ® 2016-<?php echo date("Y"); ?></h5>
												<h5>Los Angeles, California <a href="https://r2nhosting.com">R2N Hosting Solutions</a></h5>
											</center></div>
</body>
</html>
