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
        if setupinput.lower() == "#setup " + "credits " + "#window":
            print("Credits For #Window")
            print("Programming: Eryk Patocki(dunno8489@hotmail.com)")
            print("Design: Eryk Patocki(dunno8489@hotmail.com)")
            print("we know that this is open source, but use the code privately. do not use it for other oses.")
            print("<To Exit #Setup, Press Enter.>")
            setupinputcredits = input("|#Setup|#setup credits||>")
            hash_settings_status = "nonce"