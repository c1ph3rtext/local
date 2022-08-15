<!DOCTYPE html>
<html>
    <head>
        <title>
            custom server
        </title>
    <link rel="icon" href="images/dp.jpg">
    </head>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Serif&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Inconsolata:400,700|VT323" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
    <script>
          function show(){
                document.getElementById("sidebar").classList.toggle("active")
          }
    </script>
    <?php include("header.php"); ?>
    <body>
		<div id="sidebar">
              <ul>
                  <li><a href="#">Home</a></li>
                  <li><a href="resources/reso.php">Resources</a></li>
                  <li><a href="#">About</a></li>
                  <li><a href="/searchx.php">SearchX</a></li>
			  </ul>
        </div>
    </body>
</html>

