import os, sys, time
import smtplib
import random
from time import sleep as timeout
import socket
os.system("clear")
def virus():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = '''
                     .ed"""" """$$$$be.
                   -"           ^""**$$$e.
                 ."                   '$$$c        [Tools]
                /                      "4$$b
               d  3                      $$$$
               $  *                   .$$$$$$       1) DDos Attack
              .$  ^c           $$$$$e$$$$$$$$.      2) Brute Force
              d$L  4.         4$$$$$$$$$$$$$$b      3) Combo Editor
              $$$$b ^ceeeee.  4$$ECL.F*$$$$$$$      4) Website Host IP
  e$""=.      $$$$P d$$$$F $ $$$$$$$$$- $$$$$$
 z$$b. ^c     3$$$F "$$$$b   $"$$$$$$$  $$$$*"      .=""$c
4$$$$L        $$P"  "$$b   .$ $$$$$...e$$        .=  e$$$.
^*$$$$$c  %..   *c    ..    $$ 3$$$$$$$$$$eF     zP  d$$$$$
  "**$$$ec   "   %ce""    $$$  $$$$$$$$$$*    .r" =$$$$P""
        "*$b.  "c  *$e.    *** d$$$$$"L$$    .d"  e$$***"
          ^*$$c ^$c $$$      4J$$$$$% $$$ .e*".eeP"
             "$$$$$$"'$=e....$*$$**$cz$$" "..d$*"   [Cracking]
               "*$$$  *=%4.$ L L$ P3$$$F $$$P"
                  "$   "%*ebJLzb$e$$$$$b $P"        5) Reverse Text
                    %..      4$$$$$$$$$$ "          6) Cipher
                     $$$e   z$$$$$$$$$$%
                      "*$c  "$$$$$$$P"
                       ."""*$$$$$$$$bc
                    .-"    .$***$$$"""*e.
                 .-"    .e$"     "*$c  ^*b.
          .=*""""    .e$*"          "*bc  "*$e..
        .$"        .z*"               ^*$e.   "*****e.
        $$ee$c   .d"                     "*$.        3.
        ^*$E")$..$"                         *   .ee==d% [ 6virus Tool v0.5]
           $.d$$$*                           *  J$$$e*
            """""                              "$$$"

			                  '''
    for N, line in enumerate( x.split( "\n" ) ):
        sys.stdout.write( " \x1b[1;%dm%s%s\n " % (random.choice( colors ), line, clear) )
        time.sleep( 0.05 )

virus()
mawar = ("\033[31;1m")

option = input('root@root:~# ')

if option == '1':
   os.system("clear")
   os.system("python2 ddos.py")
elif option == '2':
    os.system("clear")
    print("Very Soon")

elif option == '3':
   os.system("clear")
   os.system("python3 combo.py")
elif option == '4':
    os.system("clear")
    os.system("python3 ip.py")
elif option == '5':
    os.system("clear")
    os.system("python3 Reverse.py")
elif option == '6':
    os.system("clear")
    os.system("python3 md5.py")
