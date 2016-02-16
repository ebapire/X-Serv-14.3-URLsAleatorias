#!/usr/bin/python

"""
Simple HTTP Server
Jesus M. Gonzalez-Barahona and Gregorio Robles
{jgb, grex} @ gsyc.es
TSAI, SAT and SARO subjects (Universidad Rey Juan Carlos)
"""

import socket
import random


# Create a TCP objet socket and bind it to a port
# We bind to 'localhost', therefore only accepts connections from the
# same machine
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind(('localhost', 1234))

# Queue a maximum of 5 TCP connection requests

mySocket.listen(5)

# Accept connections, read incoming data, and answer back an HTML page
#  (in an infinite loop)

try:
    while True:
        print 'Waiting for connections'
        (recvSocket, address) = mySocket.accept()
        print 'HTTP request received:'
        print recvSocket.recv(1024)
        aleatorio = random.randint(0,1000)
        respuesta1 = "HTTP/1.1 200 OK\r\n\r\n"
        html = '<html><head><h1>Hello World! </h1></head> <body><a href="HTTP://localhost:1234/' + str(aleatorio)+'">Click and come back</a> </body></html>'
        respuesta2 = "\r\n"
        recvSocket.send(respuesta1 + html + respuesta2)
        recvSocket.close()
except KeyboardInterrupt:
    print("closing socket")
    mySocket.close()
