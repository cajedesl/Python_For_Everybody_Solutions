"""
        CHAPTER 11: Regular Expressions
"""

import re

"""     Exercise 1
Write a simple program to simulate the operation of the
grep command on Unix. Ask the user to enter a regular expression and
count the number of lines that matched the regular expression:
$ python grep.py
Enter a regular expression: ^Author
mbox.txt had 1798 lines that matched ^Author
$ python grep.py
Enter a regular expression: ^X-
mbox.txt had 14368 lines that matched ^X-
$ python grep.py
Enter a regular expression: java$
mbox.txt had 4175 lines that matched java$
"""

hand = open('mbox.txt')
word = input('Enter a regular expression: ')
count = 0
for line in hand:
    line = line.rstrip()
    if re.search(word+'.*', line):
        count += 1

print('mbox.txt had %d lines that matched with %s' % (count, word))


"""     Exercise S
Write a program to look for lines of the form:
New Revision: 39772
Extract the number from each of the lines using a regular expression
and the findall() method. Compute the average of the numbers and
print out the average as an integer.
"""


fname = input('Enter the file: ')
try:
    fhand = open(fname)
except:
    print('The file cant be opened.')
    exit()

count = 0
summ = 0
average = 0
for line in fhand:
    line = line.rstrip()
    x = re.findall('^New Revision: ([0-9.]+)', line)
    if len(x) > 0:
        summ = summ + float(x[0])
        count += 1
average = summ/count
print(int(average))
