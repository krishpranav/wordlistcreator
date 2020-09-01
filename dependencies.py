import os
import time

os.system("figlet INSTALLATION")
time.sleep(1)
print("I want some depedencies so let me install it for you")
time.sleep(3)
os.system("sudo apt-get update")
os.system("sudo apt-get install figlet")
os.system("sudo apt-get install python3-pip")
os.system("pip3 install lolcat")
time.sleep(2)
os.system("figlet COMPLETED")
time.sleep(2)
print("now you can run wordlistcreate.py")
