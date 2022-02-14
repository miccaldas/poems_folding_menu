<!DOCTYPE html>
<html lang="en">
<head>
    <title>POEMS</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="author" content="Mclds">
    <meta name="description" content= 'poem page'>
    <meta property="og:title" content= >
    <meta property="og:type" content="web page">
    <meta property="og:url" content= >
    <meta property="og:image" content="../img/sun_symbol-512x512.png">
    <link rel="manifest" href="site.webmanifest">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto+Condensed:ital@1&display=swap" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="../logs/main.css" media="screen">
    <link rel="stylesheet" type="text/css" href="../logs/homepage.css" media="screen">
</head>
<br>
<?php require "../partials/header.php"; ?>
<div id="flex-container" class="flex mt=2 mb=2">
                <div id="col1" class="flex-row items-center self-center justify-center content-center w-10 order-0">
                </div>

                <div id="col2" class="flex-row items-center self-center justify-center content-center w-80 order-1">
                </div>
                    {% block content %}
                    {% endblock content %}
                <div id="col3" class="flex-row items-center self-center justify-center content-center w-10 order-2">
                </div>
            </div>
        </div>
<?php require "../partials/footer.php"; ?>
    </div>
<?php require "../partials/scripts.php" ?>
</body>
</html>
