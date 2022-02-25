# my application overview lesson

# this function should be lowercase and if more than one word
# it should have an underscore to separate each word. You should have
# a parenthesis after the name followed by a colon. Statements that are
# part of the function should be 4 spaces indented.

def my_function():
    print('hello')
    print('world')

# to run the function you must call it by name
my_function()

# when defining a function with arguments, those arguments go
# in between the parenthesis and separated by commas.

def my_other(arg1, arg2):
    print(arg1)
    print(arg2)

my_other('Red', 'Green')

# Variable Names
# - must start with a letter or an underscore
# cannot begin with a number
# can only contain alpha-numeric characters and underscores
# are case sensitive

# the variables are the left while the literal value is on the right
# value & value2 are variables
# blue and 10 are literals
# combined they are a field

value = 'Blue'
value2 = 10
print(value)
print(value2)

#variables can even change types but you might want to avoid this
value3 = 20
value3 = 'happy'
print(value3)

# multi line statements use a backslash to continue a statement on a second line
alpha = 1 + 2 + 3 \
    + 4 + 5
print(alpha)

# more than one variable on the same line
beta = 10; charlie = "python"; delta = 5
up, down, left = "town", "stairs", "right"
print(up)
print(down)
print(left)

# A class is an object, which is a blueprint. An
# instantiation of an object allows for all field and functions
# to be accessed within. Like functions outside the class,
# you need to provide 2 empty spaces before its defined
# basic class example

class MyFirstClass:
    name = 'Trever'

    def something(self):
        print('something')

my_class = MyFirstClass()
print(my_class.name)
my_class.something()

print('correction')



