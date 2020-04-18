import sys
import os
import random
import time
import hashlib
import base64
os.system("clear")
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
    print("                                      ")
    print("          [3] Hash Analyzer           ")
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
    print("                                      ")
    print("     [9] Priv8 Cipher(Can't decode)   ")
    print("                                      ")
    print("     [10] Priv8 Cipher(Can decode)    ")
    print("======================================")
    print("\n")
def choose3():
    print("\n")
    print("======================================")
    print("===========Coded by @1zsb=============")
    print("                                      ")
    print("  [1] Base64               [2] Hex    ")
    print("                                      ")
    print("          [3] Priv8 Cipher 2          ")
    print("                                      ")
    print("======================================")
    print("\n")


def incryptmd5():
    str1 = input(mawar+"insert The words to get it MD5 Hash : ")
    result1 = hashlib.md5(str1.encode())
    print("Your MD5 Hash is : ", end ="")
    print(result1.hexdigest())
    input("Done .. Press Enter To Exit ..")
def incryptsha1():
    str3 = input(mawar+"insert The words to get it SHA-1 Hash : ")
    result2 = hashlib.sha1(str3.encode())
    print("Your SHA-1 Hash is : ", end ="")
    print(result2.hexdigest())
    input("Done .. Press Enter To Exit ..")
def incryptsha224():
    str5 = input(mawar+"insert The words to get it SHA-224 Hash : ")
    result3 = hashlib.sha224(str5.encode())
    print("Your SHA-224 Hash is : ", end ="")
    print(result3.hexdigest())
    input("Done .. Press Enter To Exit ..")
def incryptsha256():
    str7 = input(mawar+"insert The words to get it SHA-256 Hash : ")
    result4 = hashlib.sha256(str7.encode())
    print("Your SHA-256 Hash is : ", end ="")
    print(result4.hexdigest())
    input("Done .. Press Enter To Exit ..")
def incryptsha384():
    str9 = input(mawar+"insert The words to get it SHA-384 Hash : ")
    result5 = hashlib.sha384(str9.encode())
    print("Your SHA-384 Hash is : ", end ="")
    print(result5.hexdigest())
    input("Done .. Press Enter To Exit ..")
def incryptsha512():
    str11 = input(mawar+"insert The words to get it SHA-512 Hash : ")
    result6 = hashlib.sha512(str11.encode())
    print("Your SHA-512 Hash is : ", end ="")
    print(result6.hexdigest())
    input("Done .. Press Enter To Exit ..")
def encodebase64():
    message1 = input(mawar+"insert The words to get it Base64 Hash : ")
    message_bytes1 = message1.encode('ascii')
    base64_bytes1 = base64.b64encode(message_bytes1)
    base64_message1 = base64_bytes1.decode('ascii')
    print("Your Base64 hash is : "+ base64_message1)
    input("Done .. Press Enter To Exit ..")
def decodebase64():
    message2 = input(mawar+"insert your Base64 Hash : ")
    message_bytes2 = message2.encode('ascii')
    base64_bytes2 = base64.b64decode(message_bytes2)
    base64_message2 = base64_bytes2.decode('ascii')
    print("Your Base64 hash is : "+ base64_message2)
    input("Done .. Press Enter To Exit ..")
def encodehex():
    hex1 = input(mawar+"insert The words to get it Hex Hash : ").encode('utf-8')
    res1 = hex1.hex()
    print("Your Hex hash is : "+ res1)
    input("Done .. Press Enter To Exit ..")
def decodehex():
    hex2 = input(mawar+"insert The words to get it Hex Hash : ")
    res2 = bytes.fromhex(hex2).decode('utf-8')
    print("Your Hex hash is : "+ res2)
    input("Done .. Press Enter To Exit ..")
def priv8encode():
    pri = input("insert The Words to get it Priv8 Cipher Hash: ")
    result8 = hashlib.md5(pri.encode())
    md5 = result8.hexdigest()
    rev = md5[::-1]
    result2 = hashlib.sha1(rev.encode())
    sha1 = result2.hexdigest()
    rev1 = sha1[::-1]
    result3 = hashlib.sha224(rev1.encode())
    sha224 = result3.hexdigest()
    result4 = hashlib.sha256(sha224.encode())
    sha256 = result4.hexdigest()
    rev2 = sha256[::-1]
    result5 = hashlib.sha384(rev2.encode())
    sha384 = result5.hexdigest()
    rev3 = sha384[::-1]
    result6 = hashlib.sha512(rev3.encode())
    sha512 = result6.hexdigest()
    message_bytes1 = sha512.encode('ascii')
    base64_bytes1 = base64.b64encode(message_bytes1)
    base64_message1 = base64_bytes1.decode('ascii')
    rev4 = base64_message1[::-1]
    hex1 = rev.encode('utf-8')
    res19 = hex1.hex()
    rev5 = res19[::-1]
    result84 = hashlib.sha512(rev5.encode())
    sha5122 = result84.hexdigest()
    print("Your Priv8 Cipher is : "+sha5122)
    input("Done .. Press Enter To Exit ..")
def priv8ende():
    hex1 = input(mawar+"insert The words to get it Priv8 Cipher 2 : ").encode('utf-8')
    res1 = hex1.hex()
    rev1 = res1[::-1]
    message_bytes1 = rev1.encode('ascii')
    base64_bytes1 = base64.b64encode(message_bytes1)
    base64_message1 = base64_bytes1.decode('ascii')
    rev2 = base64_message1[::-1]
    print("Your Priv8 Cipher 2 is : "+rev2)
    input("Done .. Press Enter To Exit ..")
def decodepriv8():
    pri = input(mawar+"insert Your Priv8 Cipher 2 : ")
    rev1 = pri[::-1]
    message_bytes2 = rev1.encode('ascii')
    base64_bytes2 = base64.b64decode(message_bytes2)
    base64_message2 = base64_bytes2.decode('ascii')
    hex2 = base64_message2[::-1]
    res0 = bytes.fromhex(hex2).decode('utf-8')
    print("Your Priv8 Cipher is : "+res0)
    input("Done .. Press Enter To Exit ..")
def Analyzer():
    os.system("clear")
    cipher()
    print("/\/\/\/\/\/\/\/\/\/\/\/\/\ ")
    print("                         /")
    print(" MD5 or MD4 length = 32  \ ")
    print(" SHA1 length = 40        /")
    print(" SHA224 length = 56      \ ")
    print(" SHA256 length = 64      /")
    print(" SHA384 length = 96      \ ")
    print(" SHA512 length = 128     /")
    print("                         \ ")
    print("\/\/\/\/\/\/\/\/\/\/\/\/\/")
    print("\n")
    hash = input("[+] insert Your Hash : ")
    if len(hash) == 32:
        print("## ## ## ## ## ## ## ## ## ## ## ## #")
        print("[!] Your Hash is MD5 or MD4 Hash [!] ")
        print("")
        input("# Press Enter to Exit . . . #")
    elif len(hash) == 40:
        print("## ## ## ## ## ## ## ## ## ## ## ## #")
        print("[!] Your Hash is SHA1 [!]")
        print("")
        input("# Press Enter to Exit . . . #")
    elif len(hash) == 56:
        print("## ## ## ## ## ## ## ## ## ## ## ## #")
        print("[!] Your Hash is SHA224 [!]")
        print("")
        input("# Press Enter to Exit . . . #")
    elif len(hash) == 64:
        print("## ## ## ## ## ## ## ## ## ## ## ## #")
        print("[!] Your Hash is SHA256 [!]")
        print("")
        input("# Press Enter to Exit . . . #")
    elif len(hash) == 96:
        print("## ## ## ## ## ## ## ## ## ## ## ## #")
        print("[!] Your Hash is SHA384 [!]")
        print("")
        input("# Press Enter to Exit . . . #")
    elif len(hash) == 128:
        print("## ## ## ## ## ## ## ## ## ## ## ## #")
        print("[!] Your Hash is SHA512 [!]")
        print("")
        input("# Press Enter to Exit . . . #")
    elif "=" in hash:
        print("## ## ## ## ## ## ## ## ## ## ## ## #")
        print("[!] Your Hash is Base64 [!]")
        print("")
        input("# Press Enter to Exit . . . #")

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
    os.system("clear")
    cipher()
    choose()
    option2 = input("root@root:~# ")
elif option1 == '99':
    os.system("clear")
    os.system("python3 start.py")
if option2 == '1':
    os.system("clear")
    cipher()
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
    elif option3 == '9':
        print("\n")
        priv8encode()
    elif option3 == '10':
        print("\n")
        priv8ende()
elif option2 == '2':
    os.system("clear")
    cipher()
    choose3()
    option4 = input("root@root:~# ")
    if option4 == '1':
        print("\n")
        decodebase64()
    elif option4 == '2':
        print("\n")
        decodehex()
    elif option4 == '3':
        print("\n")
        decodepriv8()
elif option2 == '3':
    Analyzer()
