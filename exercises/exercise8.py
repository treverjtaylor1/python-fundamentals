#5-8 HELLO ADMIN

usernames = ['Admin', 'Steve', 'Vinny', 'Sandra', 'Liz', 'William']

for username in usernames:
    if username == 'Admin':
        print('Hello Admin, would you like to see a status report?')
    else:
        print(f'Hello {username}, thank you for logging in again!')

#5-9 NO USERS

def no_user():
    usernames = []
    if usernames:
        for username in usernames:
            if username == 'admin':
                print('Hello Admin, would you like to see a status report?')
            else:
                print(f'Hello {username}, thank you for loggig in!')

    else:
        print('We need to find some users!')

no_user()

#5-10 CHECKING USERNAMES

def check_usernames():
    current_users = ['Steve', 'Vinny', 'Sandra', 'Liz', 'William']
    new_users = ['Frank', 'gertrude', 'marla', 'phil', 'Kevin']

    current_users_lower = [user.lower() for user in current_users]

    for new_user in new_users:
        if new_user.lower() in current_users_lower:
            print(f'sorry {new_user}, that name is taken')
        else:
            print(f'great, {new_user} is still available')

check_usernames()

#5-11 ORDINAL NUMBERS

def ordinal_num():
    numbers = list(range(1,10))

    for number in numbers:
        if number == 1:
            print('1st')
        elif number == 2:
            print('2nd')
        elif number == 3:
            print('3rd')
        else:
            print(f'{number}th')
ordinal_num()

#6-1 & #6-7

def person_info():

    people = []


    person = {
        'first_name': 'Steve',
        'last_name': 'Steven',
        'Age': 21,
        'city': 'Wichita'
        }
    people.append(person)

    person = {
        'first_name': 'Dr.',
        'last_name': 'Phil',
        'Age': 168,
        'city': 'Atlantis'
    }
    people.append(person)

    print(person['first_name'])
    print(person['last_name'])
    print(person['Age'])
    print(person['city'])

    for person in people:
        name = f"{person['first_name'].title()} {person['last_name'].title()}"
        age = person['Age']
        city = person['city'].title()
        print(f"{name}, of {city} is {age} years old.")
person_info()










