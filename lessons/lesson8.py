# lesson 8

# list collection
# ordered collection that can be changeable and allow
# duplicates and uses square brackets to define collected data

colors = ['red', 'blue', 'green', 'purple', 'magenta', 'black']

sizes = [42, 32, 156, 89, 34, 23, 8, 19]

mixed = [23, 'happy', 'python', 90, 45, 'snow', 'car', 56]

def simple_print():
    print(colors)

simple_print()

def simple_single():
    print(sizes[3])


simple_single()

def simple_for_print():
    for mix in mixed:
        print(mix)
simple_for_print()


# range of the list
# range of values in a list is the same is in the strings

def simple_range():
    print(colors[2:5])
    print(colors[-5:-2])

simple_range()

# using len to get the length of a list

def simple_length():
    my_colors = len(colors)
    print(len(colors))
    value = 0
    while value < my_colors:
        print(colors[value])
        value += 1

simple_length()

# using in keyword to search a list for the item
def simple_search():
    if 89 in sizes:
        print('89 is in the list')
    else:
        print('89 is not in the list')

simple_search()

#append and insert into a list
# append will insert at the end of the list

def simple_append():
    mixed.append('friday')
    for mix in mixed:
        print(mix)
simple_append()

def simple_insert():
    mixed.insert(3, 'friday')
    for value in mixed:
        print(value)

simple_insert()

# removing items from a list using remove(), pop()
# del and clear()

def simple_remove():
    colors.remove('green')
    for color in colors:
        print(color)

# simple_remove()

# the pop method will remove an item from a specified index
# not picking an index will take the last item

def simple_pop():
    colors.pop(5)
    for value in colors:
        print(value)

simple_pop()

def simple_del():
    del colors[3]
    for color in colors:
        print(color)

simple_del()

#def simple_del_none():
  #  trucks = ['chevy', 'ford', 'dodge']
   # del trucks
   # trucks.append('Toyota')
    #for value in trucks:
     #   print(value)

# simple_del_none()

def simple_clear():
    mixed.clear()
    for mix in mixed:
        print(mix)

simple_clear()



def simple_join():
    values1 = [1,2,3,4]
    values2 = [5,6,7,8]
    total = values1 + values2
    for val in total:
        print(val)

simple_join()

def simple_repeat():
    values = [1,2,3]
    print(values * 3)

simple_repeat()

def simple_membership():
    result = 'red' in colors
    print(result)
simple_membership()

def simple_iterate():
    for color in colors:
        print(color, end=' ')

simple_iterate()

my_fruits = ('apple', 'banana', 'cherry', 'orange')
# print(my_fruits)

def simple_tuple():
    for fruit in my_fruits:
        print(fruit)

        print(my_fruits[-3:-1])

simple_tuple()

def simple_change_tuple():
    fruity = list(my_fruits)
    fruity.append('peach')
    my_fruit = tuple(fruity)
    for fruit in my_fruit:
        print(fruit)

simple_change_tuple()

ice_cream = {'chocolate', 'vanilla', 'strawberry', 'neopolitan',
             'chocolate chip', 'rocky road','cookie dough'}

def simple_set():
    for flavor in ice_cream:
        print(flavor)

simple_set()

def simple_set_add():
    ice_cream.add('bunny tracks')
    for value in ice_cream:
        print(value)

simple_set_add()

def simple_set_update():
    ice_cream.update({'butter pecan', 'bunny tracks','peanut butter cup'})
    for flavor in ice_cream:
        print(flavor)

simple_set_update()


def simple_set_remove():
    num_windows = {34, 23, 78, 98, 37}
    num_windows.remove(98)
    for num in num_windows:
        print(num)

def simple_set_discard():
    letters = {'a', 'b', 'c', 'd', 'e', 'f'}
    letters.discard('a')
    for letter in letters:
        print(letter)

simple_set_discard()

def simple_set_pop():
    letters = {'a', 'b', 'c', 'd', 'e', 'f'}
    letters.pop()
    for alpha in letters:
        print(alpha)

simple_set_pop()


even = {2,4,6,8,10}
odd = {1,3,5,7,9}
tens = {10,20,30,40,50}

def simple_set_join():
    even.update(odd)
    for num in even:
        print(num)

simple_set_join()


def simple_set_union():
    values = tens.union(odd)
    for item in values:
        print(item)

simple_set_union()

def simple_set_pipe():
    numbers = odd | even | tens
    for val in numbers:
        print(val)

simple_set_pipe()


trucks = {101: 'silverado', 102: 'f150', 103: 'ram'}
print(trucks)
#print(trucks.get[103])
trucks[104] = 'titan'
print(trucks)
trucks[102] = 'f250'
print(trucks)


def simple_dict_loop():
    for truck in trucks:
        print(truck)

simple_dict_loop()

def simple_dict_square():
    for truck in trucks:
        print(trucks[truck])

simple_dict_square()

def simple_dict_values():
    for some in trucks.values():
        print(some)

simple_dict_values()

def simple_dict_both():
    for able, beta in trucks.items():
        print(able, ' - ', beta)

simple_dict_both()

my_pallet = {'color': {'primary': 'red', 'secondary': 'maroon'},
             'color2': {'primary': 'blue', 'secondary': 'royal'}}

def simple_dict_multi():
    for col1, col2 in my_pallet.items():
        print(col1, ' - ', col2)

simple_dict_multi()