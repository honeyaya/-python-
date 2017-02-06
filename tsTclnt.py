#!/usr/bin/env python

from socket import *

HOST = 'localhost' // 可以换成另外的ip
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST , PORT)

tcpCliSock = socket(AF_INET , SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
        data = raw_input('>')
        if not data:
                break
        tcpCliSock.send(data)
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
                break
        print data

tcpCliSock.close()
