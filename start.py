#!/usr/bin/python2

import os,sys,time,socket,commands,getpass

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s_ip="192.168.1.11"
s_port=8888

print "cloud services loaded ,Please enter the authentication details "
time.sleep(2)

s_user=raw_input("enter username :")
#s_user for username of client

s_password=getpass.getpass(" enter password: ")
#s_password for password of client

s.sendto(s_user,(s_ip,s_port))
s.sendto(s_password,(s_ip,s_port))

s_data=s.recvfrom(2)

if s_data[0] == "OK" :
	print "authenticated "
	print "wait for cloud services "
	os.system('echo '+s_password+'| passwd '+s_user+' --stdin')
	#echo 123 | passwd test --stdin
	time.sleep(2)
	execfile('saas.py')
else :
	print "wrong username or password !"
	exit()



