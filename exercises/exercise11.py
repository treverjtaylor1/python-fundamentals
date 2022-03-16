#9-6

class Restaurant():

    def __init__(self, name, food_type):
        self.name = name.title()
        self.food_type = food_type
        self.number_served = 0

    def describe_restaurant(self):
        message = f"{self.name} serves tasty {self.food_type}."
        print(f"\n{message}")

    def open_restaurant(self):
        message = f"{self.name} is open. Come on in!"
        print(f"\n{message}")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        self.number_served += additional_served


class IceCreamStand(Restaurant):

    def __init__(self, name, food_type='ice_cream'):
        super().__init__(name, food_type)
        self.flavors = []

    def icecream_flavors(self):
        print("\nWe have these flavors available:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")


los_icecream = IceCreamStand('Los Ice Cream Hermanos')
los_icecream.flavors = ['vanilla', 'chocolate', 'strawberry']

los_icecream.describe_restaurant()
los_icecream.icecream_flavors()

# 9-7

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


class Admin(User):

    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = []

    def show_privileges(self):
        print("\nPrivileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


steven = Admin('Steven', 'Johnson', 'sjohnson', 'sjohnson@gmail.com', 'wichita')
steven.describe_user()

steven.privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]

steven.show_privileges()

# 9-8

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


class Admin(User):

    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)

        # Initialize an empty set of privileges.
        self.privileges = Privileges()


class Privileges():

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- This user has no privileges.")

steven = Admin('steven', 'johnson', 'sjohnson', 'sjohnson@gmail.com', 'wichita')
steven.describe_user()

steven.privileges.show_privileges()

print("\nAdding privileges...")
steven_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
steven.privileges.privileges = steven_privileges
steven.privileges.show_privileges()

