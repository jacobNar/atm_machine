# This is the main ATM program, this will call all other classes and modules.

class Atm(object):
    _id = "12345"

    @property
    def id(self):
        return self._id

    def __init__(self):
        print("Atm initialized")

    def display_welcome(self):
        # console = console_library.Console()
        print("Welcome to our very expensive bank!")
