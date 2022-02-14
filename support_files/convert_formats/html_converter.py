"""Module that will convert all md files into html, using pandoc"""
import os
import subprocess

from loguru import logger

fmt = "{time} - {name} - {level} - {message}"
logger.add("/usr/share/nginx/html/poems_folding_menu/logs/info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)
logger.add("/usr/share/nginx/html/poems/folding_menu/logs/error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)


# @logger.catch
@logger.catch
def convert():
    """I'll be using pandoc as shell command as it is easier than programming it,
    to convert them to html. Then I'll change their names to PHP."""

    folder = "/usr/share/nginx/html/poems_folding_menu/support_files/poems_markdown/"
    paths = []
    for filename in os.listdir(folder):
        if filename.endswith(".md"):
            paths.append(os.path.join(folder, filename))
        else:
            continue

    for path in paths:
        filename = os.path.basename(path)
        html_url = filename[:-3] + ".html"
        logger.info(html_url)
        cmd = "pandoc --highlight-style=zenburn " + filename + " -o " + html_url
        logger.info(cmd)
        subprocess.run(cmd, cwd=folder, shell=True)

    for filename in os.listdir(folder):
        if filename.endswith(".html"):
            build_file = open(folder + filename, "r")
            build_str = build_file.read()
            out_name = filename[:-4] + "php"
            metadata_name = filename[:-4]
            out_file = open(out_name, "w")
            out_file.write(
                """<!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <title>"""
            )
            out_file.write(metadata_name)
            out_file.write(
                """
                        </title>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <meta name="author" content="Mclds">
                        <meta name="description" content="page">
                        <meta property="og:title" content='"""
            )
            out_file.write(metadata_name)
            out_file.write(
                """'>
                        <meta property="og:type" content="web page">
                        <meta property="og:url" content="">
                        <meta property="og:image" content="../img/sun_symbol-512x512.png">
                        <link rel="manifest" href="site.webmanifest">
                        <link rel="stylesheet" type="text/css" href="http://localhost/poems_folding_menu/css/homepage.css" media="screen">
                    </head>
                    <body class="vh-100 pa0 ma0 sans-serif roboto f4 fw6 dark-gray bg-near-white">
                        <div id="page_container" class="relative min-h-100 overflow-hidden db">
                            <div id="content_wrap" class="pb3">
                                <div id="top-spacer" class="h4 mt0.5 mb4">
                                <?php require '../partials/header.php'; ?>
                                </div>

                                <div id="flex-container" class="flex mt=2 mb=2">
                                    <div id="col1" class="flex-row items-center self-center justify-center content-center w-10 order-0">
                                    </div>

                                    <div id="col2" class="flex-row items-center self-center justify-center content-center w-80 order-1">
                    """
            )
            out_file.write("\n")
            out_file.write(build_str)
            out_file.write("\n")
            out_file.write(
                """
                    </div>

                                <div id="col3" class="flex-row items-center self-center justify-center content-center w-10 order-2">
                                </div>
                            </div>
                        </div>
                    </div>
                    <?php include '../partials/footer.php'; ?>
                <script src="/poems_folding_menu/support_files/js/vendor/modernizr-3.11.2.min.js"></script>
                <script src="/poems_folding_menu/support_files/js/plugins.js"></script>
                <script src="/poems_folding_menu/support_files/js/main.js"></script>
                </body>
                </html>
                """
            )
            out_file.close()
            build_file.close()

            cmd = f"mv {folder}{out_name} /usr/share/nginx/html/poems_folding_menu/pages/"
            subprocess.run(cmd, shell=True)


if __name__ == "__main__":
    convert()
