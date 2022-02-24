print("hello Worl")
# 1.  Can you make a typo that doesn’t generate an error?
# Answer: made typo in world, didn't generate an error

# 2. Can you make a typo that generates an error?
# Answer: made type in the word print and python couldn't run the file because the function wasn't spelled correctly

# 3. Why do you think it didn’t make an error?
# any typos between the quotation marks will not generate error messages
# ______________________ Question 1 Above ______________________ #

# 2. ZEN OF PYTHON
# The basis of the "Zen of Python" is that python is designed
# to be straight forward and to the point. It was written by
# python pythoneer Tim Peters in 2004. It says errors are easy to find
# and fix. Tim says if it's easy it's probably a good thing!

# 3. VARIABLES _______
message = "Hello World"
print(message)
# What I did was I assigned a 'variable' to the print function and
# the print function will print whatever I type in for the variable.
message1 = "Nice to see you today"
print(message, message1)
# This will print both message and message 1.
# I can make the variable(s) whatever I want them to be.

# 4. FUNCTIONS ________
# 8-1 MESSAGE
def display_message():
    """Display a message detailing the chapter"""
    print("I am learning about functions in this chapter")

display_message()

# 8-2 FAVORITE BOOK

def favorite_book(book):
    """Display their favorite book"""
    print(f"My favorite book is {book}!")

favorite_book('Python Crash Course')

# What I did in these exercises for # 4 is I defined functions display_message
# and favorite_book and when I call those functions they appear.

def greet_user(username):
    """Display a simple greeting"""
    print(f"Hello, {username}!")

greet_user('Jessie')




