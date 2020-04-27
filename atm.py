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

    # @property
    # def card_number(self):
    #     return self.card_number
    
    # @card_number.setter
    # def card_number(self):
    #     self.card_number = self.read_card()

    @property
    def balance(self):
        self._account.balance

    def __init__(self):
        print("Atm initialized")
        self.display_welcome()
        self._account = Account()

    def display_welcome(self):
        # console = console_library.Console()
        print("Welcome to our very expensive bank!")

    def deposit(self, deposit):
        self._account.deposit(deposit)

    # def read_card(self):
    #     return console.pin()

    # def start_session(self):
    #     self.session = session_library.Session(self._id, self.card_number)
    #     print("Session started.")

    # def end_session(self):
    #     self.session.end_session(self.session)
    #     print("Session Ended.")
    
    # def start_customer_console(self):
    #     self.customer_console = customer_console_library.Console()
    #     print("Console started.")
    
    # def get_action(self):
    #     self.action = self.customer_console.get_action()

    # def deposit_withdrawal_transfer(self):
    #     if self.action == "deposit":
    #         account.deposit()
    #     elif self.action == "withdrawal":
    #         account.withdrawal()
    #     elif self.actioin == "transfer":
    #         account.transfer()
    #     else:
    #         print("Invalid action, please try again.")
            


    
            


