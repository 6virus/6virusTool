import sys
import os
import time
import socket

def menu():
    print("======================================")
    print("===========Coded by @1zsb=============")
    print("                                      ")
    print("  [1] Start            [99]Main Menu  ")
    print("                 ==                   ")
    print("======================================")


def ip():
    print(" __  _______  ")
    print("/  |/       \ ")
    print("$$/ $$$$$$$  |")
    print("/  |$$ |__$$ |")
    print("$$ |$$    $$/ ")
    print("$$ |$$$$$$$/  ")
    print("$$ |$$ |      ")
    print("$$ |$$ |      ")
    print("$$/ $$/       ")
    print("\n")


ip()
menu()
option = input("root@root:~# ")
if option == '1':
    added = input("Domain Target: ")
    res = socket.gethostbyname(added)
    print("HOST IP : "+res)

elif option == '99':
    os.system("clear")
    os.system("python3 start.py")
