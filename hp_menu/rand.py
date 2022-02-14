"""Randomizes the poem names that appear in the homepage menu."""
import random
import subprocess

import isort  # noqa: F401
import snoop
from jinja2 import Environment, FileSystemLoader, Template  # noqa: F401
from loguru import logger

fmt = "{time} - {name} - {level} - {message}"
logger.add("../logs/info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)  # noqa: E501
logger.add("../logs/error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)  # noqa: E501

subprocess.run(["isort", __file__])


@logger.catch
@snoop
def rand():
    """We'll use a file with all the poems titles as base to randomly
    select 5 names for the menu. We'll use the library 'random' for
    the first part. The changes to the page we'll be done by a
    rewrite of the page."""

    menu_poems = []
    poem_lst = open("poem_list.txt", "r")
    lst = poem_lst.readlines()
    for i in random.sample(lst, 4):
        clean_title = i.rstrip()
        menu_poems.append(clean_title)
    poem_lst.close()
    ran0 = menu_poems[0]
    ran1 = menu_poems[1]
    ran2 = menu_poems[2]
    ran3 = menu_poems[3]

    env = Environment(loader=FileSystemLoader("/usr/share/nginx/html/poems_folding_menu/support_files/templates"))
    template = env.get_template("hp_menu.tpl")
    with open("/usr/share/nginx/html/poems_folding_menu/index.php", "w") as f:
        f.write(template.render(ran0=ran0, ran1=ran1, ran2=ran2, ran3=ran3))


if __name__ == "__main__":
    rand()
