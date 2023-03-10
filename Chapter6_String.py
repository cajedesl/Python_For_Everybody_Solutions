"""
    Chapter 6: Strings
"""

"""     Exercise 1
Write a while loop that starts at the last character in the
string and works its way backwards to the first character in the string,
printing each letter on a separate line, except backwards.
"""

word = "This is a string"
count = len(word)-1
while count >= 0:
    letter = word[count]
    print(letter)
    count -= 1


"""     Exercise 3
Encapsulate this code in a function named count, and gen-
eralize it so that it accepts the string and the letter as arguments.
"""

# we could also add a lowercase and searche the letter independently of the upper or lower case


def look_letter(word, letter_searched):
    count = 0
    new_word = word.lower()
    new_letter = letter_searched.lower()
    for letter in new_word:
        # for letter in word:
        if letter == new_letter:
            # if letter == letter_searched:
            count += + 1
    print(count)


word = "String is a string"
look_letter(word, 'S')


"""     Exercise 4
There is a string method called count that is similar to the function
in the previous exercise. Read the documentation of this method at:
https://docs.python.org/library/stdtypes.html#string-methods
Write an invocation that counts the number of times the letter a occurs in “ba-
nana”.
"""

word = 'banana'
number_letterA = word.count('a')
print(number_letterA)

"""     Exercise 5
Take the following Python code that stores a string:
str = 'X-DSPAM-Confidence:0.8475'
Use find and string slicing to extract the portion of the string after the
colon character and then use the float function to convert the extracted
string into a floating point number.
Exercise 6: Read the documentation of the string methods at
https://docs.python.org/library/stdtypes.html#string-methods You
might want to experiment with some of them to make sure you
understand how they work. strip and replace are particularly useful.
"""

str = 'X-DSPAM-Confidence:0.8475'

