# Gets user input and output for ATM.
import sys


class Console(object):

    def __init__(self, pin, choice, id):
        """ Creates Console object
        :param pin:
        :param choice:
        :param id:
        """
        self._pin = pin
        self._choice = choice
        self._id = id
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

    @classmethod
    def console_get_card_identification(cls):
        """ Gets card identification from user input
        :return:
        """
        id = int(input("Enter card ID: "))
        print("Valid card ID!")
        return id

    @classmethod
    def console_get_pin(cls):
        """ Asks user for PIN number
        :return pin:
        """
        while True:
            pin = int(input("Enter PIN: "))
            if pin < 1000 or pin > 9999:
                print("Invalid PIN")
                continue
            else:
                print("Valid PIN!")
            return pin

    @classmethod
    def console_display_menu(cls):
        """ Gets user input and displays menu for deposit, withdraw, and transfer
        :return:
        """
        print("\n1 - Deposit \t 2 - Withdraw \t 3 - Transfer \t 4 - Exit")
        choice = int(input("Select an option: "))
        if choice == 4:
            print("Thank you for choosing our very expensive bank. Have a nice day!")
            sys.exit()
        while True:
            if choice == 1:
                deposit = float(input("Enter amount to deposit: "))
                verify_deposit = input("Is this the correct amount, Yes or No?:  " + '$' + str(deposit))
                if verify_deposit == "Y" or verify_deposit == "y":
                    print("Deposit verified!")
                    break
                else:
                    print("Incorrect deposit amount")
                    continue
            elif choice == 2:
                withdraw = float(input("Enter amount to withdraw: "))
                verify_withdraw = input("Is this the correct amount, Yes or No?: " + '$' + str(withdraw))
                if verify_withdraw == "Y" or verify_withdraw == "y":
                    print("Withdraw verified!")
                    break
                else:
                    print("Incorrect withdraw amount")
                    continue
            elif choice == 3:
                transfer = float(input("Enter amount to transfer: "))
                verify_transfer = input("Is this the correct amount, Yes or No?: " + '$' + str(transfer))
                if verify_transfer == "Y" or verify_transfer == "y":
                    print("Transfer verified!")
                    break
                else:
                    print("Incorrect transfer amount")
                    continue

