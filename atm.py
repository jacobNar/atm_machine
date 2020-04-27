# This is the main ATM program, this will call all other classes and modules.

# import session as session_library
# import card_reader as card_reader_library
# import console
# import operator_panel as operator_panel_library
# import log
from account import Account
# import network as network_library
# import receipt as receipt_library

class Atm(object):
    _id = "12345"
    _account = None

    @property
    def id(self):
        return self._id

    @property
    def balance(self):
        self._account.balance

    def __init__(self):
        print("Atm initialized")
        self.display_welcome()
        self._account = Account()

    def display_welcome(self):
        print("Welcome to our very expensive bank!")

    def deposit(self, deposit):
        self._account.deposit(deposit)

    
            


    
            


