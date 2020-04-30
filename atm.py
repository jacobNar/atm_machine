# This is the main ATM program, this will call all other classes and modules.

import account
import customer

# import session as session_library
# import card_reader as card_reader_library
# import console
# import operator_panel as operator_panel_library
# import log
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
        return self._account.balance

    def __init__(self):
        print("Atm initialized")
        self.display_welcome()
        self._account = account.Account()

    def display_welcome(self):
        # This should be a console.welcome rather than a direct print.
        print("Welcome to our very expensive bank!")

    def deposit(self, deposit):
        self._account.deposit(deposit)
    
    def withdrawal(self, withdrawal):
        self._account.withdrawal(withdrawal)
    

if __name__ == "__main__":
    """ testing """
    atm = Atm()
    atm.deposit(100)
    print(atm.balance)
    atm.withdrawal(50)
    print(atm.balance)
    
            


    
            


