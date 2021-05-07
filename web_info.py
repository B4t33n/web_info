print("\033[92m")
import os
import urllib2
import sys

print("---------------------------------------------")

os.system("figlet web info")

print("----------------------------------------------")
print("\033[91m")


print("#############################################")
print("               Coded by B4t33n               ")
print("#############################################")

print("\033[93m")
print("             INFORMATION                     ")

print(".............................................")
print("")

print("   FB PAGE      : https://www.facebook.com/B4t33n/")
print("   CODER        : B4t33n")
print("   VERSION      : 1.0")
print("   TEAM         : BWHH")
print("   EMAIL        : gamilniyakikorbu@gmail.com")

print("\033[92m")
print(">>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<")
print("\033[91m")

print("   Enter CTRL+Z To Exit Tool                       ")

print("")
print("\033[94m")
url = raw_input(">>>>ENTER YOUR WEBSITE LINK :")

print("\033[95m")
print("")
url.rstrip ( )
print("")
header = urllib2.urlopen (url) .info ( )
print("")
print(str (header) )