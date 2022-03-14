#8-3

def make_shirt(size, message):
    print(f"\nI'm going to make a {size} shirt")
    print(f"it will say '{message}'")

make_shirt("medium", "cool guy behind shirt")
make_shirt(message="don't read this shirt", size= "medium")

#8-4

def make_shirt(size='Large', message='Dont read this shirt'):
    print(f"\nI'm going to make a {size} shirt")
    print(f"it will say '{message}'")

make_shirt()
make_shirt(size='medium')
make_shirt('small', 'please read this shirt.')

#8-5

def describe_city(city, country="united states"):
    message = f"{city.title()} is in {country.title()}."
    print(message)

describe_city('wichita')
describe_city('reykjavik', 'iceland')
describe_city('Kansas City')

#8-9
def show_messages(messages):
    for message in messages:
        print(message)

messages = ["hi", "hope you are well", "have a good day"]
show_messages(messages)


#8-10 & 8-11
def show_messages(messages):
    print("Showing all messages:")
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    print("\nSending all messages:")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

messages = ["hi", "hope you are well", "have a good day"]
show_messages(messages)

sent_messages = []
send_messages(messages[:], sent_messages)

print("\nFinal lists:")
print(messages)
print(sent_messages)

#9-1 & 9-2
class Restaurant():

    def __init__(self, name, food_type):
        self.name = name.title()
        self.food_type = food_type

    def describe_restaurant(self):
        message1 = f"{self.name} serves tasty {self.food_type}."
        print(f"\n{message1}")

    def open_restaurant(self):
        message1 = f"{self.name} is open for business. Come on in."
        print(f"\n{message1}")

restaurant = Restaurant('Los Pollos Hermanos', 'chicken')
print(restaurant.name)
print(restaurant.food_type)

restaurant.describe_restaurant()

pollos_hermanos = Restaurant('Los Pollos Hermanos', 'Chicken')
pollos_hermanos.describe_restaurant()

lombardis = Restaurant('Lombardis', 'Pizza')
lombardis.describe_restaurant()

sumo_grill = Restaurant('Sumo Grill', 'Hibachi')
sumo_grill.describe_restaurant()

#9-3 USERS

class User():

    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        print(f"\nWelcome back, {self.username}!")

steven = User('steven', 'johnson', 'sjohnson', 'sjohnson@gmail.com', 'wichita')
steven.describe_user()
steven.greet_user()

Phil = User('Dr.', 'Phil', 'docphil', 'waxhead@hotmail.com', 'the moon')
Phil.describe_user()
Phil.greet_user()


#9-4

class Restaurant():

    def __init__(self, name, food_type):
        self.name = name.title()
        self.food_type = food_type

    def describe_restaurant(self):
        message1 = f"{self.name} serves tasty {self.food_type}."
        print(f"\n{message1}")

    def open_restaurant(self):
        message1 = f"{self.name} is open for business. Come on in."
        print(f"\n{message1}")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        self.number_served +=additional_served

restaurant = Restaurant('Los Pollos Hermanos', 'chicken')
restaurant.describe_restaurant()

print(f"\nNumber served: {restaurant.number_served}")
restaurant.number_served = 80
print(f"Number served: {restaurant.number_served}")

restaurant.set_number_served(75)
print(f"Number served: {restaurant.number_served}")

restaurant.increment_number_served(90)
print(f"Number served: {restaurant.number_served}")


# 9-5
class User():


    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        print(f"\nWelcome back, {self.username}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

eric = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()
eric.greet_user()

print("\nMaking 3 login attempts...")
eric.increment_login_attempts()
eric.increment_login_attempts()
eric.increment_login_attempts()
print(f"  Login attempts: {eric.login_attempts}")

print("Resetting login attempts...")
eric.reset_login_attempts()
print(f"  Login attempts: {eric.login_attempts}")

