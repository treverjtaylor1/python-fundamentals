#1. 2-8 THE NUMBER EIGHT

print(5+3)
print(10-2)
print(4*2)
print(16/2)

fav_number = 26
print(f'My favorite number is {fav_number}')

val1 = 456_234
val2 = 68_423_791
val3 = 13_794_628
val4 = 96_374

#2.
def number_sets():
    print(val1)
    print(val2)
    print(val3)
    print(val4)

number_sets()

#3.

def number_arg():
    arg1 = 34
    arg2 = 34.5

    print(float(arg1))
    print(int(arg2))

number_arg()

#4.

def favorite_movie():
    Favorite = input('What is your favorite movie?')
    Times = input('How many times have you seen it?')
    message = 'I have seen {0} ''{1} times'
    print(message.format(Favorite, Times))

favorite_movie()




