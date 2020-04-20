class Account(object):
    """Includes balance property, __init__, withdrawal and deposit
    methods.

    """
    # _account_number = 123
    # _balance = 0
    # _withdrawal_limit = 400

    @property
    def balance(self):
        """Gets account balance.

        Returns:
            account balance (data type?)

        """
        return self.balance

    def __init__(self, account_number = 123, balance = 0, withdrawal_limit = 400):
        """Creates an account object.
        
        Args:
            account_number (?): Optional for now?
            balance (?): zero
            withdrawal_limit (?): $400

        """
        self.balance = balance
        self.account_number = account_number
        self.withdrawal_limit = withdrawal_limit

    def withdrawal(self, withdrawal):
        """Checks if balance is positive, higher than withdrawal amount
        and if withdrawal amount is less than withdrawal limit. If all
        conditions are true, acount balance is being updated to reflect
        the withdrawal. If no, detailed error messages are displayed.

        """
        if self.balance > 0 and self.balance >= withdrawal and withdrawal <= self.withdrawal_limit:
            self.balance -= withdrawal

        if self.balance <= 0:
            print("You don't have enough funds to complete the transaction." +
                  f" Your balance is {self.balance}.")
        if withdrawal > self.balance:
            print("You can't withdraw more funds than you have available. " +
                  f"Your balance is {self.balance}.")
        if withdrawal > 400:
            print("Your withdrawal request has been denied. ATM daily " +
                  "withdrawal limit is $400.00. You have requested " +
                  f"{withdrawal}.")
        if withdrawal <= 0:
            print("Your withdrawal amount must be a positive number. "
                  f"{withdrawal} is not valid.")

    def deposit(self, deposit):
        self.balance += deposit

if __name__ == "__main__":
    """Run tests if module is executed by name."""
    account = Account()
    # print("Balance:", account.balance)
