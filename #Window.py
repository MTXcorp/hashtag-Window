import os as sys
from FhashWindow import FhashWindow

SessionStatus = "define"
Version = " V2.0"
Name = "#Window"
TypeCmd = "in cmd"
rootUserName = "change_me"
rootPassword = "changeme"



def clean():
    if sys.name == "nt":
        sys.system("cls")
    else:
        sys.system("clear")
def Folder():
    sys.system("dir")
def text_edit():
    clean()
SessionStatus = "Cleaning"
clean()
SessionStatus = "in cmd"
print("#Window V2.0")
while SessionStatus == "in cmd":
    cmdinput = input("|>")
    if cmdinput.lower() == "version":
        print(Name + Version)
    if cmdinput.lower() == "exit":
        clean()
        exit("Exiting Python And #Window...")
    if cmdinput.lower() == "supercmd " + "exit":
        hashcallinput = input("|Password of " + rootUserName + ":|>")
        if hashcallinput.lower() == rootPassword:
           clean()
           exit("[root]" + "Exiting Python And #Window...")
        else:
            print("Try Again!")
    if cmdinput.lower() == "files":
        sys.system("dir")
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
    if cmdinput.lower() == "all version":
        print("FhashWindow Version: " + FhashWindow.Version)
        print("#Window Version: " + Version)