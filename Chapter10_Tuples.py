"""
        Chapter 10: Tuples
"""
import time
import os
import string

"""     Exercise 1
Revise a previous program as follows: Read and parse the
“From” lines and pull out the addresses from the line. Count the num-
ber of messages from each person using a dictionary.
After all the data has been read, print the person with the most commits
by creating a list of (count, email) tuples from the dictionary. Then
sort the list in reverse order and print out the person who has the most
commits
"""
"""     Exercise 2
This program counts the distribution of the hour of the day
for each of the messages. You can pull the hour from the “From” line
by finding the time string and then splitting that string into parts using
the colon character. Once you have accumulated the counts for each
hour, print out the counts, one per line, sorted by hour as shown below.
"""

fname = input('Enter the name of the file: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    exit()

counts_mail = dict()
counts_hours = dict()
for line in fhand:
    words = line.split()
    if len(words) == 0 or words[0] != 'From':
        continue
    hours = words[5].split(':')
    if words[1] not in counts_mail:
        counts_mail[words[1]] = 1
    else:
        counts_mail[words[1]] += 1
    if hours[0] not in counts_hours:
        counts_hours[hours[0]] = 1
    else:
        counts_hours[hours[0]] += 1

lst = list()
# taking the values of the dict and transforming
for key, value in list(counts_mail.items()):
    lst.append((value, key))                    # in a list of tuple

lst.sort(reverse=True)
print(lst[0][1], lst[0][0])

list_hours = list()
for key, value in list(counts_hours.items()):
    list_hours.append((key, value))

list_hours.sort()
print(list_hours)

time.sleep(3)
os.system('cls')


"""     Exercise 3
Write a program that reads a file and prints the letters
in decreasing order of frequency. Your program should convert all the
input to lower case and only count the letters a-z. Your program should
not count spaces, digits, punctuation, or anything other than the letters
a-z. Find text samples from several different languages and see how
letter frequency varies between languages. Compare your results with
the tables at https://wikipedia.org/wiki/Letter_frequencies.
"""

counts = 0
counts_let = dict()
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.translate(str.maketrans('', '', string.digits))
    words = line.lower()
    if len(words) == 0:
        continue
    for word in words:      # cada palavra dentro da lista de palavras
        for letter in word:  # eu pego cada letra dentro dela
            counts += 1
            if letter not in counts_let:
                counts_let[letter] = 1
            else:
                counts_let[letter] += 1

listat = list()
for key, value in list(counts_let.items()):
    listat.append((value, key))

listat.sort(reverse=True)

for key, value in listat:  # printing the percentage value
    print((key/counts)*100, value)
