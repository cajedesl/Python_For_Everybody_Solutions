"""    Chapter 12: Networked Programs
"""
import urllib.error
import urllib.parse
import urllib.request
import socket
from bs4 import BeautifulSoup
import ssl
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


"""     Exercise 3
Use urllib to replicate the previous exercise of (1) retrieving
the document from a URL, (2) displaying up to 3000 characters, and
(3) counting the overall number of characters in the document. Don’t
worry about the headers for this exercise, simply show the first 3000
characters of the document contents.
"""

url = input('Enter URL: ')

try:
    fhand = urllib.request.urlopen(url)
except:
    print('Impossible to connect: improperly formatted or non-existent URL.')
    exit()

count = 0

for line in fhand:
    line = line.decode().rstrip()
    count += len(line)
    # if count <= 3000:
    #    print(line[:3000-count-1])
    if count > 3000:
        break
    print(line)
print('Count: ', count)

time.sleep(3)
os.system('cls')

"""     Exercise 4
Change the urllinks.py program to extract and count para-
graph (p) tags from the retrieved HTML document and display the
count of the paragraphs as the output of your program. Do not display
the paragraph text, only count them. Test your program on several
small web pages as well as some larger web pages.
"""

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the paragraph tags

tags = soup('p')
count = 0
for tag in tags:
    # print(tag)
    count += 1
    # print(tag.get('href', None))

print('The number of paragraph tag is: ', count)


time.sleep(3)
os.system('cls')

"""     Ecercise 5
(Advanced) Change the socket program so that it only shows
data after the headers and a blank line have been received. Remember
that recv receives characters (newlines and all), not lines.
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

file = b""
count = 0
while True:
    data = mysocket.recv(512)
    if len(data) < 1:
        break
    count += len(data)
    file += data
    # print(data.decode(), end='')

new_file = file.split(b"\r\n\r\n")

print(new_file[1].decode())

mysocket.close()
