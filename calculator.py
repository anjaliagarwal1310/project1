#!/usr/bin/python

import os,sys,time,socket,commands,getpass

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s_ip="192.168.1.11"
s_port=8888

os.system('ssh -X test@'+s_ip+' gnome-calculator')

execfile('saas.py')
