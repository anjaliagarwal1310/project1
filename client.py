#!/usr/bin/python2

import os,sys,commands,socket,time

sip="192.168.1.10"
sport=4444

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

user=raw_input("enter username :")
password=raw_input("enter user password :")

s.sendto(user,(sip,sport))
s.sendto(password,(sip,sport))

print s.recvfrom(100)

while True:
	cmd=raw_input("[root@station10 ]# ")
	s.sendto(cmd,(sip,sport))
	#print s.recvfrom(100)[0]

