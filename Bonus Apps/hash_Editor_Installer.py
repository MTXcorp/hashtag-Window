import os as sys

def clean():
    if sys.name == "nt":
        sys.system("cls")
    else:
        sys.system("clear")
clean()
print("Hash Editor Installer For Hash Window.")
print("1=Install")
print("2=Uninstall")
print("3=Exit")
UniverInput = input("|Hash Editor Installer|>")
if UniverInput == '1':
    clean()
    print("Installing...")
    content = open("hash_Editor", "w")
    content.write("import ComponentList as CList\n")