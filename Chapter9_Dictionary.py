"""
    Chapter 9: Dictionaries
"""
import time
import os
import string as sg

"""     Exercise 1: Download a copy of the file www.py4e.com/code3/words.tx
Write a program that reads the words in words.txt and stores them as
keys in a dictionary. It doesn\’t matter what the values are. Then you
can use the in operator as a fast way to check whether a string is in the
dictionary"""

words_dic = dict()
file = open("words.txt")
for line in file:
    words = line.split()
    # print(words)
    for i in words:
        words_dic[i] = 'a'      # any value

print(words_dic)

print('Writing' in words_dic)

time.sleep(3)
os.system('cls')

"""     Exercise 2
Write a program that categorizes each mail message by
which day of the week the commit was done. To do this look for lines
that start with “From”, then look for the third word and keep a running
count of each of the days of the week. At the end of the program print
out the contents of your dictionary (order does not matter).
"""
"""     Exercise 3
Write a program to read through a mail log, build a his-
togram using a dictionary to count how many messages have come from
each email address, and print the dictionary.
"""
"""     Exercise 4
Add code to the above program to figure out who has the
most messages in the file. After all the data has been read and the dic-
tionary has been created, look through the dictionary using a maximum
loop (see Chapter 5: Maximum and minimum loops) to find who has
the most messages and print how many messages the person has
"""

#   I solved the 3 questions above in the same code bellow:
fname = input('Enter the name of the file: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    exit()

counts_day = dict()
counts_mail = dict()
for line in fhand:
    words = line.split()
    if len(words) == 0 or words[0] != 'From':
        continue
    if words[2] not in counts_day:
        counts_day[words[2]] = 1
    else:
        counts_day[words[2]] += 1
    if words[1] not in counts_mail:
        counts_mail[words[1]] = 1
    else:
        counts_mail[words[1]] += 1

largest = None
emaim = None
for key in counts_mail:
    if largest == None or counts_mail[key] > largest:
        largest = counts_mail[key]
        email = key

print(counts_day)
print(counts_mail)
print(email, largest)

time.sleep(3)
os.system('cls')

#
"""     Exercise 5
This program records the domain name (instead of the
address) where the message was sent from instead of who the mail came
from (i.e., the whole email address). At the end of the program, print
out the contents of your dictionary.
"""

fname = input('Enter the name of the file: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    exit()

counts_mail = dict()
for line in fhand:
    words = line.split()
    if len(words) == 0 or words[0] != 'From':
        continue
    indice_arroba = words[1].index('@')
    domaine = words[1][indice_arroba+1:]
    if domaine not in counts_mail:
        counts_mail[domaine] = 1
    else:
        counts_mail[domaine] += 1

print(counts_mail)
