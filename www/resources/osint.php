<!DOCTYPE>
<html>
<head>
<script src="https://kit.fontawesome.com/a076d05399.js" crossorigin="anonymous"></script>
<title>Osint</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<link href="https://fonts.googleapis.com/css?family=Inconsolata:400,700|VT323" rel="stylesheet">
<link rel="stylesheet" href="../style.css">
<?php include("../header.php"); ?>
</head>
<body class="osi-body" style="background: url('https://wallpapercave.com/wp/wp10215527.jpg') fixed no-repeat center; background-size: cover">
<div class="osin"><h1><i class="fa fa-search-plus"></i>  Osint online tools<h1></div>
<div class="osi">
<ul>
  <li><a target="_blank" href="https://osintframework.com/">Osint Framework</a></li>
  <li><a onclick="fun()" href="#">Osint Tricks</a></li>
</ul>
  <div class="content hide">
  osint techniques<br><br>
  [+] Use Osint Framework to Collect Infos<br>
  [+] To Collect Subdomains: "site: *.target.com"<br>
  [+] Create Sock puppet to Gather info from social medias<br>
  [+] recon What you Collected<br>
  [+] for osint tools go to : <a href="https://www.osinttechniques.com/osint-tools.html" target="_blank">Online tools</a><br>
  [+]  Extract metadata : <a href="https://brandfolder.com/workbench/extract-metadata">Extract Metadata</a>
  </div>
  <script>
       x = document.querySelector(".content");
       function fun(){
			x.classList.toggle("hide");
       }
  </script>
</div>
</body>
</html>
