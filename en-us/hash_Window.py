import os as sys
import hash_Settings
import hash_Window_Config
import ComponentList as CList

SessionStatus = "define"
Version = " V2.0"
Name = "#Window"
TypeCmd = "in cmd"
#Super User Credentials
rootUserName = "change_me"
rootPassword = "changeme"
#User Credentials
UserUserName = "user"
UserPassword = "changeme"


SessionStatus = "Cleaning"
CList.clean.clean()
SessionStatus = "reqlogon"
print("#Window V2.0 Logon")
usernameinput = input("|Username:|>")
if usernameinput == hash_Window_Config.UserUserName:
    passwordinput = input("|Password:|>")
    if passwordinput == UserPassword:
        CList.clean.clean()
        SessionStatus = "in cmd"
        print("#Window V2.0")
while SessionStatus == "in cmd":
    
    cmdinput = input("|>")
    if cmdinput.lower() == "version":
        print(Name + Version)
    if cmdinput.lower() == "exit":
        CList.clean.clean()
        exit("Exiting Python And #Window...")
    if cmdinput.lower() == "supercmd " + "exit":
        hashcallinput = input("|Password of " + rootUserName + ":|>")
        if hashcallinput.lower() == rootPassword:
            CList.clean.clean()
            exit("[root]" + "Exiting Python And #Window...")
        else:
            print("Try Again!")
    if cmdinput.lower() == "files":
        CList.folder.folder()
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
        CList.clean.clean()
    if cmdinput.lower() == "setup":
        CList.clean.clean()
        hash_Settings.settings()
    if cmdinput.lower() == "bash-mode":
        SessionStatus = "bshmod"
        while SessionStatus == "bshmod":
            bashinput = input("|BASH Mode|>")
            if bashinput == "exit bash-mode":
                SessionStatus = "in cmd"
            else:
                sys.system(bashinput)
    if cmdinput.lower() == "move":
        print("Mover Tool 1.2 (exit to Quit Mover.)")
        print("What File To Move?")
        moveinput1 = input("|Mover Tool 1.2|>")
        if moveinput1 == "exit":
            moveinput2 = input("|Press Enter To Exit.|>")
        else:
            print("Where To Move?")
            moveinput2 = input("|Mover Tool 1.2|>")
            sys.system("move " + moveinput1 + moveinput2)
    if cmdinput.lower() == "file manager":
        while SessionStatus == "File Manager":
            print("#Hash File Manager - /b Style - Drive C:")
            sys.system("dir /b")
            hashfilemanagerinput1 = input("|Hash File Manager|>")
