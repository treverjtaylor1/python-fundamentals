# lesson 9 classes and functions

class cat:
    # class variable
    kind = 'feline'

    # cosntructor
    def __init__(self, name, color):
        # instance variables
        self.name = name
        self.color = color

    # basic method
    def cat_color(self):
        return self.color

    def cat_name(self):
        return self.name

# object creation

my_cat = cat('Felix', 'white')
my_other = cat('Garfield', 'orange')

# name is unique to the created object

print(my_cat.cat_name())
print(my_other.cat_color())
print(my_other.cat_color())
print(my_cat.name)
print(my_other.name)

# kind is shared by all created objects
print(my_other.kind)

# function review

def my_fancy_functions(arg, arg2):
    print(arg + ' = ' + arg2)

my_fancy_functions('Friday', 'Fun')
my_fancy_functions(arg2= 'Weekend', arg= 'Saturday')

def my_favorite_color(*colors):
    print('my favorite color is ' + colors[1])

my_favorite_color('red', 'green', 'blue')

# tuple of colors
# *args takes a tuple in values but not as a variable, you will generate
# an error if you push a tuple value directly

# favs = ('red', 'blue', 'yellow')
# fav2 = ('green', 'orange')
# my_favorite_color(favs, fav2)

# using **kwargs will allow a dictionary of arguments

def vehicles(**truck):
    print('my truck is a ' + truck['model'])

vehicles(make= 'chevy', model='silverado')

def my_hello(arg, arg2='hi'):
    print(arg2 + ' ' + arg)

my_hello('tom')
my_hello('Tim', 'Hello')


def simple_add(value1, value2):
    return value1 + value2

total = simple_add(12, 23)
print(total)
print(simple_add(5,10))

