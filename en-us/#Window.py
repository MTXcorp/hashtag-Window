import os as sys
from hash_Settings import hash_Settings
from hash_Components import clean
from hash_Components import folder
SessionStatus = "define"
Version = " V2.0"
Name = "#Window"
TypeCmd = "in cmd"
rootUserName = "change_me"
rootPassword = "changeme"
UserUserName = "MySQL"
UserPassword = "rah"


SessionStatus = "Cleaning"
clean.clean()
SessionStatus = "reqlogon"
print("#Window V2.0 Logon")
usernameinput = input("|Username:|>")
if usernameinput == UserUserName:
    passwordinput = input("|Password:|>")
    if passwordinput == UserPassword:
        clean.clean()
        SessionStatus = "in cmd"
        print("#Window V2.0")
while SessionStatus == "in cmd":
    
    cmdinput = input("|>")
    if cmdinput.lower() == "version":
        print(Name + Version)
    if cmdinput.lower() == "exit":
        clean.clean()
        exit("Exiting Python And #Window...")
    if cmdinput.lower() == "supercmd " + "exit":
        hashcallinput = input("|Password of " + rootUserName + ":|>")
        if hashcallinput.lower() == rootPassword:
            clean.clean()
            exit("[root]" + "Exiting Python And #Window...")
        else:
            print("Try Again!")
    if cmdinput.lower() == "files":
        folder.folder()
    if cmdinput.lower() == "supercmd " + "files":
        hashcallinput = input("|Password of " + rootUserName + ":|>")
        if hashcallinput == rootPassword:
            sys.system("dir")
        else:
            print("Try Again!")
    if cmdinput.lower() == "supercmd " + "version":
        hashcallinput = input("|Password of " + rootUserName + ":|>")
        if hashcallinput == rootPassword:
            print(Version)
        else:
            print("Try Again!")
    if cmdinput.lower() == "version " + "all":
        print("#Window Version: " + Version)
    if cmdinput.lower() == "cleanup":
        clean.clean()
    if cmdinput.lower() == "setup":
        clean()
        