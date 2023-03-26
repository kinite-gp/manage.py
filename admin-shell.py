import readline
from os import system
from colorama import Fore, init
from json import load

path = open("path.json","r")
path = load(path)

print(path)
init()

paths = path["path"]
manage = path["manage.py"]

addrs = ['runserver',
         'createsuperuser',
         "check",
         "compilemessages",
         "createcachetable",
         "dbshell",
         "diffsettings",
         "dumpdata",
         "flush",
         "inspectdb",
         "loaddata",
         "makemessages",
         "makemigrations",
         "migrate",
         "optimizemigration",
         "shell",
         "showmigrations",
         "sqlflush",
         "sqlmigrate",
         "sqlsequencereset",
         "squashmigrations",
         "startapp",
         "startproject",
         "test",
         "testserver",
         "collectstatic",
         "findstatic",
         "clearsessions",
         "changepassword",
         "remove_stale_contenttypes",
         ]

            

def completer(text, state):
    options = [x for x in addrs if x.startswith(text)]
    try:
        return options[state]
    except IndexError:
        return None


readline.set_completer(completer)
readline.parse_and_bind("tab: complete")

while 1:
    try:
        command = input(Fore.BLUE + "python manage.py ")
        print(' ' + Fore.RESET)
        system(paths + f" {manage} " + command)
    except KeyboardInterrupt:
        print("\nKeyboard interrupted !!!\n")
        