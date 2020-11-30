#!/bin/python3

import socket

HOST = '127.0.0.1'  #making portscanner
PORT = 7777

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))


#root@kali:~# nc -nvlp 7777 
#listening on [any] 7777 ...
#connect to [127.0.0.1] from (UNKNOWN) [127.0.0.1] 59728

