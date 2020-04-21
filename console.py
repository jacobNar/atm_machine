# Gets user input for ATM


class Console:
    def __init__(self, pin_number, menu_choice, amount):
        self.pin = pin_number
        self.choice = menu_choice
        self.amount = amount


def pin():
    pin_number = int(input("Enter pin: "))
    print(pin_number)


def menu():
    print("\n1 - Deposit \t 2 - Withdraw \t 3 - Transaction")
    menu_choice = int(input("Enter a number: "))
    print(menu_choice)
