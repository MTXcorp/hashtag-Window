import os as sys


__name__ = "hash_settings"
Version = "V1.0"

def settings():
    hash_settings_status = "in settings()"
    while hash_settings_status == "in settings()":
       if sys.name == "nt":
            sys.system("cls")
       else:
           sys.system("clear")
    print("#hash Settings#############")
    print("##General##################")
    print("##1 = Program List>      ##")
    print("##2 = Version>           ##")
    print("###########################")
    print("###########################")
    settingsinput1 = input("|Hash Settings> |>")