import sys

# Gets user input and output for ATM.


class Console(object):
    amount = 0

    def __init__(self, pin, choice, amount, id):
        """ Creates Console object
        :param pin:
        :param choice:
        :param amount:
        :param id:
        """
        self.pin = pin
        self.choice = choice
        self.amount = amount
        self.id = id
        print("Console created")


def get_pin():
    """ Asks user for PIN number
    :return pin:
    """
    pin = int(input("Enter PIN: "))
    if pin < 1000 or pin > 9999:
        print("Invalid PIN")
        pin = None  # Might add loop if pin = None so user can enter valid PIN.
    else:
        print("Valid PIN!")
        # pin = True
    print(pin)  # An ATM usually does not print PIN. Printing PIN to make sure input works. Will remove it.
    return pin


def get_card_identification():
    id = int(input("Enter your card ID: "))
    print(id)  # Printing to make sure input works.
    # Will add error handling based on what a card ID should look like


def get_choice():
    print("\n1 - Deposit \t 2 - Withdraw \t 3 - Transfer")
    choice = int(input("Select an option: "))
    return choice


def display_menu(choice):
    """ Displays menu for deposit, withdraw, and transfer
    :return:
    """
    if choice == 1:
        deposit = float(input("Enter amount to deposit: "))
        verify_deposit = input("Is this the correct amount, Yes or No ? " + str(deposit))
        if verify_deposit == "Y":
            print("Deposit verified!")
        else:
            sys.exit()
            # Add error handling
    elif choice == 2:
        withdraw = float(input("Enter amount to withdraw: "))
        verify_withdraw = input("Is this the correct amount, Yes or No ? " + str(withdraw))
        if verify_withdraw == "Y":
            print("Withdraw verified!")
        else:
            sys.exit()
            # Add error handling
    elif choice == 3:
        transfer = float(input("Enter amount to transfer: "))
        verify_transfer = input("Is this the correct amount, Yes or No ? " + str(transfer))
        if verify_transfer == "Y":
            print("Transfer verified!")
        else:
            sys.exit()
            # Add error handling


if __name__ == '__main__':
    console = Console
