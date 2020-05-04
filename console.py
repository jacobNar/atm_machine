# Gets user input and output for ATM.
import sys


class Console(object):
    _choice = None
    _id = None
    _pin = None
    
    def __init__(self):
        """ Creates Console object
        :param pin:
        :param choice:
        :param id:
        """
        print("Console created")

    @ property
    def pin(self):
        return self._pin

    @ property
    def choice(self):
        return self._choice

    @ property
    def id(self):
        return self._id

    def get_card(self):
        """ Gets card identification from user input
        :return:
        """
        self._id = input("Enter card ID: ")
        print("Valid card ID!")
        return self.id

    def get_pin(self):
        """ Asks user for PIN number
        :return pin:
        """
        while True:
            pin = input("Enter PIN: ")
            print(pin)
            if len(pin) != 4:
                print("Invalid PIN")
                continue
            else:
                print("Valid PIN!")
            self._pin = pin
            return self.pin

    def display_menu(self):
        """ Gets user input and displays menu for deposit, withdraw, and transfer
        :return:
        """
        print("\n1 - Deposit \t 2 - Withdraw \t 3 - Transfer \t 4 - Exit")
        choice = input("Select an option: ")
        if choice == "4":
            print("Thank you for choosing our very expensive bank. Have a nice day!")
            sys.exit()
        while True:
            if choice == "1":
                deposit = float(input("Enter amount to deposit: "))
                verify_deposit = input("Is this the correct amount, Yes or No?:  " + '$' + str(deposit))
                if verify_deposit == "Y" or verify_deposit == "y":
                    print("Deposit verified!")
                else:
                    print("Incorrect deposit amount")
                    continue
                choices = [choice, deposit]
                return choices

            elif choice == "2":
                withdraw = float(input("Enter amount to withdraw: "))
                verify_withdraw = input("Is this the correct amount, Yes or No?: " + '$' + str(withdraw))
                if verify_withdraw == "Y" or verify_withdraw == "y":
                    print("Withdraw verified!")
                else:
                    print("Incorrect withdraw amount")
                    continue

                choices = [choice, withdraw]
                return choices

            elif choice == "3":
                transfer = float(input("Enter amount to transfer: "))
                verify_transfer = input("Is this the correct amount, Yes or No?: " + '$' + str(transfer))
                if verify_transfer == "Y" or verify_transfer == "y":
                    print("Transfer verified!")
                    
                else:
                    print("Incorrect transfer amount")
                    continue

                choices = [choice, transfer]
                return choices

        self._choice = choice


if __name__ == "__main__":
    console = Console()
    id = console.get_card()
    pin = console.get_pin()
    choice = console.display_menu()
    print(id, pin, choice)
