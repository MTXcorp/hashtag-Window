import ComponentList as CList
import hash_Window_Config as HWConfig
import os as sys
import time as clock

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
    print()