#Name:          UDP Pinger Client Core
#Student:       Joshua Nguyen 1304578

from socket import *
from datetime import datetime
from time import time
import os



def main():
    sName = 'LOCALHOST'
    sPort = 12000
    clientSocket = socket(AF_INET,SOCK_DGRAM)
    message = 'Ping'
    counter = 10
    x = 0
    remain = counter - x
    print (counter, "pings are being used. \n")
    
    while x < counter:
        x+=1
    print ("\nPrinting attempt number", x , "is currently in working in progress.\n")
    print (remain, "attempts remain.\n")
    date = datetime.now()
    clientSocket.sendto(message,(sName,sPort))

    ########################################
    clientSocket.settimeout(1)
    
    try:
        modifiedMessage,serverAddress = clientSocket.recvfrom(1024)
        date2 = datetime.now()
        rt = date - date2;
        print (modifiedMessage)
        print ("Time that elapsed: ", rt,microseconds, "microsecs\n")
        
    except timeout:
        print ("Sorry! Your connection has timed out! Please try again later! ")
        
    if x == 10:
        print ("Bye Bye!!")
        clientSocket.close()

    os.system("pause")
pass

if __name__ == '__main__':
    main()














































