# This is the main ATM program, this will call all other classes and modules.

import account
import customer

# import session as session_library
# import card_reader as card_reader_library
import console as console_library
# import operator_panel as operator_panel_library
# import log
# import network as network_library
# import receipt as receipt_library

class Atm(object):
    _id = "12345"
    _account = account.Account()
    _customer = None
    _console = console_library.Console()
    _card = None
    _pin = None

    @property
    def id(self):
        return self._id

    @property
    def balance(self):
        return self._account.balance

    def __init__(self):
        print("Atm initialized")
        self.display_welcome()

    def display_welcome(self):
        # This should be a console.welcome rather than a direct print.
        print("Welcome to our very expensive bank!")
        self._card = self._console.get_card()
        self._pin = self._console.get_pin()
        self.display_menu()
    
    def deposit(self, deposit):
        self._account.deposit(deposit)
    
    def log_in(self, card_id, pin):
        self._customer = customer.Customer()
        self._customer.validate(card_id, pin)
        self._account = account.Account()

    def withdrawal(self, withdrawal):
        self._account.withdrawal(withdrawal)

    def display_menu(self):
        choice = self._console.display_menu()
        print(choice)

        if(choice[0] == "1"):
            self.deposit(choice[1])
            print("Balance:" , self.balance)
        elif(choice[0] == "2"):
            self.withdrawal(choice[1])
            print("Balance:" , self.balance)
        elif(choice[0] == "3"):
            # self.transfer(self._choice[1])
            print("Balance:" , self.balance)
        

    

if __name__ == "__main__":
    """ testing """
    atm = Atm()
    # atm.log_in("1111111111", "1111")

    # atm.deposit(100)
    # print(atm.balance)
    # atm.withdrawal(50)
    # print(atm.balance)

    
