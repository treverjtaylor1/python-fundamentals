# boolean
# these values are either true or false
def boolean_sample():
    print(bool('sample'))
    print(bool(0.0))

# boolean_sample()

# if statement
# used to find out if a condition is true

def basic_if(arg1, arg2):
    if arg1 > arg2:
        print('are value is greater than our other one')

    if arg1 == arg2:
        print('both values are the same')

basic_if(10,5)


#elif example
# used when the first condition is false and you want to try another

def basic_if_elif(arg):
    if arg > 10:
        print('sum is greater than 10')
    elif arg == 10:
        print('sum is the 10')
    elif arg <= 10:
        print('sum is less than 10')

basic_if_elif(10)

# else statement
# this keyword can be used to execute a block of code
# when the if statement results are false

def else_example(arg):
    if arg > 15:
        print('Our argument is greater than 15')
    else:
        print('our argument is less than 15')

else_example(12)

#else with elif
def check_grade(arg):
    if arg == 'A':
        print('Excellent')
    elif arg == 'B':
        print('Good')
    elif arg == 'C':
        print('average')
    elif arg == 'D':
        print('Below average')
    elif arg == 'F':
        print('Failed')
    else:
        print('not a valid grade')

# check_grade(input('What is your grade?'))

#Nested if statement
# This allows an if statement to be inside another if statement
# the inner if statement only evaluates if the outer if is true.

def nested_example(arg):
    if arg:
        print('happy is greater than the argument')
        if arg > 30:
            print('happy is greater than 30')
        else:
            print('happy is less than 30')

nested_example(4)

#ternary statement
# one condition can be performed on one line
# basically a shorthand if statement
golf = 42
hotel = 24

# if shorthand
result = golf if golf > hotel else hotel
print(result)

print("both are equal" if golf == hotel else 'golf is greater' if golf
      > hotel else "hotel is greater")

def if_short_decoded():
    if golf == hotel:
        print('both are equal')
    elif golf > hotel:
        print('golf is greater')
    else: print('hotel is greater')

if_short_decoded()

# and & or keyword
def combined(arg1, arg2, arg3):
    if arg1 > arg2 and arg1 >= arg3:
        print('argument 1 is the greatest')

    if arg2 > arg3 or arg2 <= arg3:
        print('argument 2 is greater than 3 but not 1')

    combined(30, 20, 30)





