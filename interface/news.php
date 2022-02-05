<html><head><meta charset="UTF-8"/>
  		<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
			<link rel="stylesheet" type="text/css" href="style.css"/><link rel="stylesheet" type="text/css" href="nav.css"/><link rel="stylesheet" type="text/css" href="sidebar.css"/>
      <link href="http://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
      <title>Black Hole Search</title>
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
              <a href="https://github.com/diveyez">Contact Developer</a>
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

<!--ROADMAP CHECKLIST -->
						<div id="roadmap">
						<ul><h3><b>Planned Features:</b></h3></li></br>
							<li>[x] Plotly & Finviz Charts</li></br>
							<li>[?] </li></br>
							<h5><b>'x'</b> Indicates nearly full or full completion, periods <b>'.'</b> mark the in progress. </br>
							<b>'?'</b> Indicates that there is no available information on completion date.</h5></br></div>
<!--ROADMAP CHECKLIST -->
<!-- FOOTER AREA -->
						<div id="footer"><center>
								<h5> <a href="https://github.com/diveyez">Black Hole</a> by <a href="https://github.com/diveyez">'Diveyez' </a></p>&copy; ® 2016-<?php echo date("Y"); ?></h5>
												<h5>Los Angeles, California <a href="https://titantrades.com">TitanTrades.com</a></h5>
											</center></div>
