# 5-1 TRUE CONDITIONAL STATEMENTS
#1.
#true
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

#false
print("\nIs car == 'Audi'? I predict true.")
print(car == 'audi')

#true
animal = 'horse'
print("The animal is a 'horse'.")
print(animal == 'horse')

#false
print("\n the animal is a 'dog'.")
print(animal == 'dog')

#true
object = 'fork'
print("The object in question is a 'fork'")
print(object == 'fork')

#false
print('The object is a "spoon".')
print(object == 'spoon')

#true
computer = 'macbook'
print("the computer is a 'macbook'.")
print(computer == 'macbook')

#false
print('I think the computer is a "PC"')
print(computer == 'PC')

#true
table = 'coffee table'
print('the table is a "coffee table"')
print(table == 'coffee table')

#false
print('the table is a "Kitchen Table"')
print(table == 'Kitchen table')

#5-2 CONDITIONAL TESTS CONT.
# 1. INEQUALITY IN STRINGS
num = '6'
print(num == '5')
# 2. .lower() method
car = 'bugatti'
print(car == 'Bugatti'.lower())
# 3. numeric tests
num1 = '7'
print(num1 == '7')
print(num1 != '8')
print(num1 >= '9')
print(num1 <= '8')
# 4. and / or statements
echo = 6
delta = 5

def and_statement():
    result = echo > 5 and delta < 10
    print(result)
def or_statement(num1):
    result = num1 > echo or num1 < delta
    print(result)

or_statement(8)

#IN list
def list_function():
    list = ['horse', 'dog', 'cat', 'boat']
    print('horse' in list)
list_function()
#NOT IN LIST
def not_list_function():
    list = ['horse', 'dog', 'cat', 'boat']
    print('dog' not in list)
not_list_function()

#_______________________
#3 Arithmetic argument function

def operator_time(sum1, sum2):
    result_add = sum1 + sum2
    result_subtract = sum1 - sum2
    result_multi = sum1 * sum2
    result_divide = sum1 / sum2
    result_greater = sum1 >= sum2
    result_less = sum2 >= sum1

operator_time(10, 5)

#4. MODULUS, MINUS, EXPONENT, PLUS
def one_arg_function(num1):
    num1 %= 24
    print(num1)
    num1 **= 75
    print(num1)
    num1 -= 10
    print(num1)
    num1 += 15
    print(num1)

one_arg_function(75)







