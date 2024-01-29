import os as sys

def clean():
    if sys.name == "nt":
        sys.system("cls")
    else:
        sys.system("clear")