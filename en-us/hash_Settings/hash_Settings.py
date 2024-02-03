import os as sys


__name__ = "hash_settings"
Version = "V1.0"

def settings():
    hash_settings_status = "in settings()"
    while hash_settings_status == "in settings()":
        sys.system("clear")
        setupinput = input("|#Setup|No_Command||>")
        if setupinput.lower() == "#setup " + "version":
            print(Version)
            setupinputversion = input("|#Setup|#setup version||>")
        if setupinput.lower() == "#setup " + "credits":
            print("You Found The Easter Egg!")
            print("Programming: Eryk Patocki(dunno8489@hotmail.com)")
            print("Design: Eryk Patocki(dunno8489@hotmail.com)")
            print("we know that this is open source, but use the code privately. do not use it for other oses.")
            setupinputcredits = input("|#Setup|#setup credits||>")
            hash_settings_status = "nonce"