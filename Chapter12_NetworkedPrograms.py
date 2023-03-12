"""    Chapter 12: Networked Programs
"""

import socket
import os
import time

"""     Exercise 1
Change the socket program socket1.py to prompt the user
for the URL so it can read any web page. You can use split('/') to
break the URL into its component parts so you can extract the host
name for the socket connect call. Add error checking using try and
except to handle the condition where the user enters an improperly
formatted or non-existent URL.
"""


url = input("Enter URL: ")

# we open a connection to the server on port 80
web_page = url.split('/')
HOST = web_page[2]
PORT = 80
try:
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.connect((HOST, PORT))
except:
    print('Impossible to connect: improperly formatted or non-existent URL.')
    exit()

# \r\n\r\n means a blank line
cmd = ('GET ' + url + ' HTTP/1.0\r\n\r\n').encode()
# then we send this get comand falloed by a blank line
mysocket.send(cmd)

while True:
    data = mysocket.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

mysocket.close()


time.sleep(3)
os.system('cls')

"""     Exercise 2
Change your socket program so that it counts the number
of characters it has received and stops displaying any text after it has
shown 3000 characters. The program should retrieve the entire docu-
ment and count the total number of characters and display the count
of the number of characters at the end of the document.
"""

url = input("Enter URL: ")

# we open a connection to the server on port 80
web_page = url.split('/')
HOST = web_page[2]
PORT = 80
try:
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.connect((HOST, PORT))
except:
    print('Impossible to connect: improperly formatted or non-existent URL.')
    exit()

# \r\n\r\n means a blank line
cmd = ('GET ' + url + ' HTTP/1.0\r\n\r\n').encode()
# then we send this get comand falloed by a blank line
mysocket.send(cmd)

count = 0

# I'm a bit confused abot what he called 3000 caracters
while True:
    data = mysocket.recv(512)
    count += len(data)
    # print(data)
    if len(data) < 1 or count > 3000:
        break
    print(data.decode(), end='')

print('Count: ', count)
mysocket.close()


time.sleep(3)
os.system('cls')
