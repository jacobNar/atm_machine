class Account(object):
    """Includes balance property, __init__, withdrawal and deposit
    methods.

    """
    _account_number = None
    _balance = None
    _withdrawal_limit = None

    @property
    def balance(self):
        """Gets account balance.

        Returns:
            account balance (data type?)

        """
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value

    def __init__(self, account_number=0, 
                 balance=0,
                 withdrawal_limit=400):
        """Creates an account object.

        Args:
            account_number
            balance: $0
            withdrawal_limit: $400

        """
        self.balance = balance
        self._account_number = account_number
        self._withdrawal_limit = withdrawal_limit

    @property
    def limit(self):
        return self._withdrawal_limit

    @property
    def number(self):
        return self._account_number

    def withdrawal(self, withdrawal):
        """Checks if balance is positive, higher than withdrawal amount
        and if withdrawal amount is less than withdrawal limit. If all
        conditions are true, acount balance is being updated to reflect
        the withdrawal. If no, detailed error messages are displayed.

        """
        if self.balance <= 0:
            raise ValueError("You don't have enough funds to complete the transaction."
                  f" Your balance is ${self.balance}.")
        
        if withdrawal > self.balance:
            raise ValueError("You can't withdraw more funds than you have available. "
                  f"Your balance is ${self.balance}. You have requested " + \
                  f"${withdrawal}.")
        
        if withdrawal > self.limit:
            raise ValueError("Your withdrawal request has been denied. ATM daily "
                  f"withdrawal limit is {self.limit}. You have requested " + \
                  f"${withdrawal}.")
        
        if withdrawal <= 0:
            raise ValueError("Your withdrawal amount must be a positive number. "
                  f"${withdrawal} is not valid.")

        self.balance -= withdrawal

    def deposit(self, deposit):
        if deposit > 0:
            self.balance += deposit
        else:
            raise ValueError(f"You may deposit positive amount only. ${deposit} is not" +
                  " valid.")

if __name__ == "__main__":
    """Run tests if module is executed by name."""
    account = Account()
    print(account.number, account.balance, account.limit)
