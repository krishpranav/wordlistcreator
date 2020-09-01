#!usr/bin/env/python

import time
import os

red='\033[91m'
b='\033[21m'
gren='\033[92m'
yellow='\033[93m'
cyan='\033[96m'
blue='\033[94m'

os.system("clear")
os.system("figlet LISTCREATOR | lolcat")
time.sleep(1)
length=int(raw_input(cyan+b+"Enter the number of character of your wordlist (infinity number) >> "+b+cyan))
print (" ")
name=raw_input(cyan+b+"Name your wordlist with (.txt) extension: "+b+cyan)
tic = time.clock()
print (" ")
print (blue+b+"================================"+b+blue)
print (" ")
print (red+b+"Generating wordlist please wait!!"+b+red)
print (" ")
print (blue+b+"================================"+b+blue)
print (" ")
lista=[0 for x in xrange(length)]
x=length-1
string="abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*"
list_of_results=[]
file1=file(name,"w")
while(x>-1):
    result=""
    if lista[x]==len(string)-1:
        for z in xrange (length):
            result+=string[lista[z]]
        lista[x]=0
        x-=1
    elif x==length-1:
        for z in xrange(length):
            result+=string[lista[z]]
        lista[x]+=1
    else:
        for z in xrange(length):
            result+=string[lista[z]]
        lista[x]+=1
        if x>0:
            x+=1
        else:
            x=length-1
    file1.write(result+"\n")
toc = time.clock()
ttn = toc - tic
print (yellow+b+"----------------------------------------------"+b+yellow)
print (" ")
print (red+b+"Wordlist created within "+str(ttn)+" seconds."+b+red)
print (" ")
print (red+b+"Wordlist Generated Successfully "+str(name)+" pleaase check in your folder"+b+red)
print (" ")
print (yellow+b+"----------------------------------------------"+b+yellow)
print (" ")
