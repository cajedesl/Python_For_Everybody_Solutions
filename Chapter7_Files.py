"""
    Chapter 7: Files
"""

"""     Exercise 1
Write a program to read through a file and print the contents
of the file (line by line) all in upper case. Executing the program will
look as follows:
python shout.py
Enter a file name: mbox-short.txt
FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN 5 09:14:16 2008
RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
SAT, 05 JAN 2008 09:14:16 -0500
"""
file = open('book_examples.txt')
for i in file:
    i = i.rstrip()
    print(i.upper())

"""     Exercise 2
Write a program to prompt for a file name, and then read
through the file and look for lines of the form:
X-DSPAM-Confidence: 0.8475
When you encounter a line that starts with “X-DSPAM-Confidence:”
pull apart the line to extract the floating-point number on the line.
Count these lines and then compute the total of the spam confidence
values from these lines. When you reach the end of the file, print out
the average spam confidence.
"""

"""     Exercise 3
Sometimes when programmers get bored or want to have a
bit of fun, they add a harmless Easter Egg to their program. Modify
the program that prompts the user for the file name so that it prints a
funny message when the user types in the exact file name “na na boo
boo”. The program should behave normally for all other files which
exist and don’t exist.
"""

name = input('Enter the name of the file: ')
try:
    file = open(name)
except:
    if name == 'na na boo boo':
        print('NA NA BOO BOO TO YOU - You have been punk\'d')
        exit()
    else:
        print('No file with this name!')
        exit()

count = 0
summ = 0
for line in file:
    if line.startswith('X-DSPAM-Confidence:'):
        count = count+1
        indexx = line.index(':')
        summ = summ + float(line[indexx+1:-1])

print('Average spam confidence: ', summ/count)
