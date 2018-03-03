#Name:      UDP Pinger Server
#Student:   Joshua Nguyen


import random
from socket import *


serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('',12000))

while True:
#This generated random number in the range from 0 to 10
    rand = random.randint(0, 10)
#Receive the client packet along with the address
    message, address = serverSocket.recvfrom(1023)
#Undermines the message from the client
    message = message.upper()
    if rand < 4:
        continue
#Otherwise, the server responds
    serverSocket.sendto(message, address)
