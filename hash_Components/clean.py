import os as sys

__name__ = "hash_components_clean"
Version = "V1.1"
def clean():
    if sys.name == "nt":
        sys.system("cls")
    else:
        sys.system("clear")