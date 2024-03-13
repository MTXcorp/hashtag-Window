import ComponentList as CList
import hash_Window_Config as HWConfig
import os as sys
import time as clock

DevSprayInput = "none"

__version__ = "1.1"
def cleanscr():
    CList.clean.clean()
def showfiles():
    CList.folder.folder()
def cursor(message_in_cursor):
    DevSprayInput = input("|" + message_in_cursor + "|>")
def ChangeDir(dir_to_change_to):
    sys.system("cd " + dir_to_change_to)
def Say(message):
    print(message)
def SayTimeLimit(message, timeLimit):
    print(message)
    clock.sleep(timeLimit)
    CList.clean.clean()
def ListVersion():
    print(__version__)
def menu(message1_1, message2_1, message3_1, message4_1, navbar_name):
    print("#" + navbar_name + "#")
    print("#1" + message1_1)
    print("#2" + message2_1)
    print("#3" + message3_1)
    print("#4" + message4_1)
    print("#8" + "Previous Page")
    print("#9" + "Next Page")