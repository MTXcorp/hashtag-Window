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
UserUserName = "user"
UserPassword = "changeme"


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
        print("#Setup Version: " + hash_Settings.Version)
    if cmdinput.lower() == "cleanup":
        clean.clean()
    if cmdinput.lower() == "setup":
        clean.clean()
        hash_Settings.settings()
    if cmdinput.lower() == "bash-mode":
        SessionStatus = "bshmod"
        while SessionStatus == "bshmod":
            bashinput = input("|BASH Mode|>")
            if bashinput == "exit bash-mode":
                SessionStatus = "in cmd"
            else:
                sys.system(bashinput)
    if cmdinput.lower() == "return to bash":
        print("To Return To #Window, Type In 'Exit'.")
        sys.system("bash")