import sys
import os
import time
import random

def combo():
    print("""
    ██████╗ ██████╗ ███╗   ███╗██████╗  ██████╗     ███████╗██████╗ ██╗████████╗ ██████╗ ██████╗
    ██╔════╝██╔═══██╗████╗ ████║██╔══██╗██╔═══██╗    ██╔════╝██╔══██╗██║╚══██╔══╝██╔═══██╗██╔══██╗
    ██║     ██║   ██║██╔████╔██║██████╔╝██║   ██║    █████╗  ██║  ██║██║   ██║   ██║   ██║██████╔╝
    ██║     ██║   ██║██║╚██╔╝██║██╔══██╗██║   ██║    ██╔══╝  ██║  ██║██║   ██║   ██║   ██║██╔══██╗
    ╚██████╗╚██████╔╝██║ ╚═╝ ██║██████╔╝╚██████╔╝    ███████╗██████╔╝██║   ██║   ╚██████╔╝██║  ██║
    ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝  ╚═════╝     ╚══════╝╚═════╝ ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                                                                                              """)

combo()
def menu():
    print("======================================")
    print("===========Coded by @1zsb=============")
    print("                                      ")
    print("  [1] Start            [99]Main Menu  ")
    print("                 ==                   ")
    print("======================================")
menu()
print("\n")
print("\n")
option = input("root@root:~# ")

mawar = ("\033[31;1m")
if option == '1':
    vi = input(mawar+"user : @")
    input("\nPress Enter To Start ..")
    print("")
    print("\nStarting ..\n\n")

    with open("passwords.txt", "r") as rf:
        with open("combo_edit.txt", "w") as wf:
            for line in rf:
                wf.write(vi + ":" + line)

                input("Done .. Press Enter to Return To Menu ..")
elif option == '99':
    os.system("clear")
    os.system("python3 start.py")
else:
    exit()
