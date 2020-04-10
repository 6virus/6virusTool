import sys
import os
import random
import time
import hashlib
import base64

mawar = ("\033[31;1m")

def menu():
    print("\n")
    print("======================================")
    print("===========Coded by @1zsb=============")
    print("                                      ")
    print("  [1] Start            [99]Main Menu  ")
    print("                 ==                   ")
    print("======================================")
    print("\n")

def choose():
    print("\n")
    print("======================================")
    print("===========Coded by @1zsb=============")
    print("                                      ")
    print("  [1] Incrypt            [2] Decrypt  ")
    print("                 ==                   ")
    print("======================================")
    print("\n")

def choose2():
    print("\n")
    print("======================================")
    print("===========Coded by @1zsb=============")
    print("                                      ")
    print("  [1] MD5       =====      [2] SHA-1  ")
    print("                                      ")
    print("   [3] SHA-224           [4] SHA-256  ")
    print("                                      ")
    print("    [5] SHA-384        [6] SHA-512    ")
    print("                                      ")
    print("      [7] Base64     [8] Hex          ")
    print("======================================")
    print("\n")
def choose3():
    print("\n")
    print("======================================")
    print("===========Coded by @1zsb=============")
    print("                                      ")
    print("  [1] Base64  ===========   [2] Hex   ")
    print("                =======               ")
    print("======================================")
    print("\n")


def incryptmd5():
    str1 = input(mawar+"insert The words to get it MD5 Hash : ")
    result = hashlib.md5(str1.encode())
    print("Your MD5 Hash is : ", end ="")
    print(result.hexdigest())
    input("Done .. Press Enter To Exit ..")
def incryptsha1():
    str3 = input(mawar+"insert The words to get it SHA-1 Hash : ")
    result = hashlib.sha1(str3.encode())
    print("Your SHA-1 Hash is : ", end ="")
    print(result.hexdigest())
    input("Done .. Press Enter To Exit ..")
def incryptsha224():
    str5 = input(mawar+"insert The words to get it SHA-224 Hash : ")
    result = hashlib.sha224(str5.encode())
    print("Your SHA-224 Hash is : ", end ="")
    print(result.hexdigest())
    input("Done .. Press Enter To Exit ..")
def incryptsha256():
    str7 = input(mawar+"insert The words to get it SHA-256 Hash : ")
    result = hashlib.sha256(str7.encode())
    print("Your SHA-256 Hash is : ", end ="")
    print(result.hexdigest())
    input("Done .. Press Enter To Exit ..")
def incryptsha384():
    str9 = input(mawar+"insert The words to get it SHA-384 Hash : ")
    result = hashlib.sha384(str9.encode())
    print("Your SHA-384 Hash is : ", end ="")
    print(result.hexdigest())
    input("Done .. Press Enter To Exit ..")
def incryptsha512():
    str11 = input(mawar+"insert The words to get it SHA-512 Hash : ")
    result = hashlib.sha512(str11.encode())
    print("Your SHA-512 Hash is : ", end ="")
    print(result.hexdigest())
    input("Done .. Press Enter To Exit ..")
def encodebase64():
    message = input(mawar+"insert The words to get it Base64 Hash : ")
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    print("Your Base64 hash is : "+ base64_message)
    input("Done .. Press Enter To Exit ..")
def decodebase64():
    message = input(mawar+"insert your Base64 Hash : ")
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64decode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    print("Your Base64 hash is : "+ base64_message)
    input("Done .. Press Enter To Exit ..")
def encodehex():
    hex1 = input(mawar+"insert The words to get it Hex Hash : ").encode('utf-8')
    res = hex1.hex()
    print("Your Hex hash is : "+ res)
def decodehex():
    hex2 = input(mawar+"insert The words to get it Hex Hash : ")
    res = bytes.fromhex(hex2).decode('utf-8')
    print("Your Hex hash is : "+ res)

def cipher():
    print("  ______   __            __                           ")
    print(" /      \ /  |          /  |                          ")
    print("/$$$$$$  |$$/   ______  $$ |____    ______    ______  ")
    print("/$$$$$$  |$$/   ______  $$ |____    ______    ______  ")
    print("$$ |      $$ |/$$$$$$  |$$$$$$$  |/$$$$$$  |/$$$$$$  |")
    print("$$ |   __ $$ |$$ |  $$ |$$ |  $$ |$$    $$ |$$ |  $$/ ")
    print("$$ \__/  |$$ |$$ |__$$ |$$ |  $$ |$$$$$$$$/ $$ |      ")
    print("$$    $$/ $$ |$$    $$/ $$ |  $$ |$$       |$$ |      ")
    print(" $$$$$$/  $$/ $$$$$$$/  $$/   $$/  $$$$$$$/ $$/       ")
    print("              $$ |                                    ")
    print("              $$ |                                    ")
    print("              $$/                                     ")
    print("\n")

cipher()
menu()
option1 = input("root@root:~# ")

if option1 == '1':
    choose()
    option2 = input("root@root:~# ")
elif option1 == '99':
    os.system("clear")
    os.system("python3 start.py")
if option2 == '1':
    choose2()
    option3 = input("root@root:~# ")
    if option3 == '1':
        print("\n")
        incryptmd5()
    elif option3 == '2':
        print("\n")
        incryptsha1()
    elif option3 == '3':
        print("\n")
        incryptsha224()
    elif option3 == '4':
        print("\n")
        incryptsha256()
    elif option3 == '5':
        print("\n")
        incryptsha384()
    elif option3 == '6':
        print("\n")
        incryptsha512()
    elif option3 == '7':
        print("\n")
        encodebase64()
    elif option3 == '8':
        print("\n")
        encodehex()
elif option2 == '2':
    choose3()
    option4 = input("root@root:~# ")
    if option4 == '1':
        print("\n")
        decodebase64()
    elif option4 == '2':
        print("\n")
        decodehex()
