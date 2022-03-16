# 9-10
from exercise9 import restaurant

Hermanos_pollos = restaurant('Hermanos Pollos', 'chicken')
Hermanos_pollos.describe_restaurant()
Hermanos_pollos.open_restaraunt()

#9-11

from exercise11 import Privileges

#9-12

from exercise9 import User


class Admin(User):

    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)

        # Initialize an empty set of privileges.
        self.privileges = Privileges()


class Privileges():

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("Privileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- This user has no privileges.")

#9-16 Read on the module of Dates and Times
