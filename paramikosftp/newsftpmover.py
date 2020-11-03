#!/usr/bin/env python3
## Moving files with SFTP

## import paramiko so we can talk SSH
import paramiko
import os

# Menu to choose which server to connect to
print("Which server would you like to connect to? Type the number and hit \'ENTER\'")
print("     1. Bender")
print("     2. Fry")
print("     3. Zoidberg") 

while True:
    try:
        server = float(input("        ~"))
        break

    except:
        print("Input does not match. Please try again.")

## where to connect to
if server == 3:
    t = paramiko.Transport("10.10.2.5", 22) 
elif server == 2:
    t = paramiko.Transport("10.10.2.4", 22)
elif server == 1:
    t = paramiko.Transport("10.10.2.3", 22)
else:
    print("Input does not match. Please try again.")

## how to connect (see other labs on using id_rsa private/public keypairs)
#t.connect(username="bender", password="alta3")
#t.connect(username="bender")

## Make an sftp connection object
#sftp = paramiko.SFTPClient.from_transport(t)

## iterate across the files within directory
#for x in os.listdir("/home/student/filestocopy/"): # iterate on directory contents
#  if not os.path.isdir("/home/student/filestocopy/"+x): # filter everything that is NOT a directory
#    sftp.put("/home/student/filestocopy/"+x, "/tmp/"+x) # move file to target location

## close the connection
#sftp.close() # close the connection

