# All about strings

# what is a string?
# A string is a sequence of characters. it can be defined with either
# single or double quotes.

# single quotes
alpha = 'hello'

# double quotes
beta = "Python"

# print results
print(alpha)
print(beta)

# a multi-line string uses three single or three double quotes and
# allows a string to be created on multiple lines.
multi = '''This string can be seen 
on multiple lines so you could do
paragraphs if necessary'''
print(multi)

# getting a specific index using the square bracket
charlie = 'happy'
print(charlie[2])

# if you put a value of an index that is higher than the number
# of characters -1 you will generate an error
# print(charlie[5])

# slicing and range of characters
# using the name square brackets, you can output a range of
# characters from a string. This is called "Slicing". You use a colon to
# separate the start and end of a slice
Delta = 'enjoy python'
print(Delta[2:5])
# output should be joy

# negative slicing we use negative numbers. Instead of starting from zero
# it begins at the end of a string.
print(Delta[-5:-2])

# What is check string
# The ability to compare a set of characters with a
# string variable. This result will be either True or False.
# we use in and not in as keywords for check string

# using in keyword
txt = 'This is a test sentence'
result1 = 'is' in txt

# using not in keyword
txt2 = 'This other phrase is a test'
result2 = 'th' not in txt2

print(result1)
print(result2)

# string concatenation in python is the ability to join 2 or more strings
# using the plus operator
# basic concatenation
cat1 = 'Happy'
cat2 = 'Friday'
combine = cat1 + cat2
print(combine)
combine2 = cat1 + ' ' + cat2
print(combine2)

cat3 = "sample"
combine3 = cat3 + ' code'
print(combine3)

# larger concatenation with more than 2 variables
combine4 = cat1 + ' ' + cat2 + ' ' + combine3
print(combine4)

#strings and a number ?
 # combine5 = cat3 + 5

# string format using a curly brace
age = 4
msg1 = 'my dog is {} years old'
print(msg1.format(age))

msg2 = 'my dog {1} is {0} years old'
print(msg2.format(age, 'Spot'))

# optional formats
name = 'John'
total = 34.9856
msg3= 'Hello {0}, your order comes to {1:6.2f}'
print(msg3.format(name, total))

# octal escape sequence '\110\145\154\154\157'






