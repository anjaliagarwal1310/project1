#!/usr/bin/python

import os,sys,time,commands,socket

x="""
press 1 to get firefox :
press 2 to get vlc :
press 3 to get calculator :
press 4 to get office :
"""

print x

ch=raw_input()

if ch == '1' :
	print "now wait for a second "
	execfile('firefox.py')

elif ch == '2' :
	print "now wait for a second "
	execfile('vlc.py')

elif ch == '3' :
	print "now wait for a second "
	execfile('calculator.py')

elif ch == '4' :
	print "now wait for a second "
	execfile('office.py')

else :
	print "wrong choice"
