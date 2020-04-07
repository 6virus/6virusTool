import os
import sys
import random
import time
os.system("clear")
def main():
    print("======================================")
    print("===========Coded by @1zsb=============")
    print("                                      ")
    print("  [1] Start            [99]Main Menu  ")
    print("                 ==                   ")
    print("======================================")


def rev():
    print(" ________                      __     ")
    print("|        \                    |  \    ")
    print(" \$$$$$$$$______   __    __  _| $$_   ")
    print("   | $$  /      \ |  \  /  \|   $$ \  ")
    print("   | $$ |  $$$$$$\ \$$\/  $$ \$$$$$$  ")
    print("   | $$ | $$    $$  >$$  $$   | $$ __ ")
    print("   | $$ | $$$$$$$$ /  $$$$\   | $$|  \ ")
    print("   | $$  \$$     \|  $$ \$$\   \$$  $$")
    print("    \$$   \$$$$$$$ \$$   \$$    \$$$$ ")
    print("                                      ")
rev()
main()

option = input("root@root:~# ")
if option == '1':
    print("-------------------")
    txt = input("Put Your Text: ")

    res = txt[::-1]
    print("Your Text Reverse : " + res)
    input("Done ... Press Enter To Exit ..")
elif option == '99':
    os.system("clear")
    os.system("python3 start.py")
