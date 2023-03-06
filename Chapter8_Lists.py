"""
    Chapter 8: Lists
"""
import time
import os
import string

"""     Exercise 1
Write a function called chop that takes a list and modifies
it, removing the first and last elements, and returns None. Then write
a function called middle that takes a list and returns a new list that
contains all but the first and last elements.
"""


def chop(t):
    del t[0]
    del t[len(t)-1]


def middle(lista):
    return lista[1:len(lista)-1]


lst1 = [1, 2, 3, 4]
lst2 = [1, 2, 3, 4]

chop(lst1)

print(lst1)
print(middle(lst2))

time.sleep(3)
os.system('cls')

#
"""     Exercise 3
Rewrite the guardian code in the above example without
two if statements. Instead, use a compound logical expression using
the or logical operator with a single if statement.
"""
file = open('book_examples.txt')
for line in file:
    words = line.split()
    # print('Debug: ', words)
    if len(words) == 0 or words[0] != 'From':
        continue
    # if words[0]!= 'From' or len(words)==0: continue
    print(words[2])

time.sleep(3)
os.system('cls')

""" Exercise 4
Download a copy of the file www.py4e.com/code3/romeo.txt.
Write a program to open the file romeo.txt and read it line by line. For
each line, split the line into a list of words using the split function.
For each word, check to see if the word is already in a list. If the word
is not in the list, add it to the list. When the program completes, sort
and print the resulting words in alphabetical order.
"""

file = open('romeo.txt')
lst__ = list()
for line in file:
    line = line.translate(str.maketrans('', '', string.punctuation))
    words = line.split()
    for word in words:
        # print(word)
        if word in lst__:
            continue
        lst__.append(word)

lst__.sort()
print(lst__)

time.sleep(3)
os.system('cls')

"""     Exercise 5
Write a program to read through the mail box data and
when you find line that starts with “From”, you will split the line into
words using the split function. We are interested in who sent the
message, which is the second word on the From line.
"""
file = open('book_examples.txt')
cont = 0
for line in file:
    words = line.split()
    # print('Debug: ', words)
    if len(words) == 0 or words[0] != 'From':
        continue
    # if words[0]!= 'From' or len(words)==0: continue
    print(words[1])
    cont = cont + 1

print('There were', cont, ' lines in the file with From as the first word')

time.sleep(3)
os.system('cls')

"""     Exercise 6
Rewrite the program that prompts the user for a list of
numbers and prints out the maximum and minimum of the numbers at
the end when the user enters “done”. Write the program to store the
numbers the user enters in a list and use the max() and min() functions to
compute the maximum and minimum numbers after the loop completes.
"""
list1 = []
while True:
    number = input('Enter a number: ')
    if number == 'done':
        break
    list1.append(int(number))

print(list1)
print('Maximum:', max(list1))
print('Minimim: ', min(list1))
