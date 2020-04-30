# Customer module to handle customer information such as name, card number, pin, and account number

class Customer(object):
    """Customer class for ATM

    Att: 
        name (string): customer first/last name
        card_id (string): customer card number
        pin (string): customer pin
        accounts (list): list of account numbers
        is_validated (bool): card number and pin validation/session

    """
    _customers = []
    _name = None
    _card_id = None
    _pin = None
    _is_validated = False  #session control: logged in with card/pin
    _accounts = []

    @property
    def list(self):
        result = "Name,Card,Pin,Accounts\n"
        for customer in self._customers:
            result += f"{customer['name']},{customer['card_id']}," \
                f"{customer['pin']},{customer['accounts']}\n"
        return result

    @property
    def name(self):
        """Gets customer name

        Returns:
            name (string)
        
        """
        return self._name

    @property
    def is_validated(self):
        """Gets session activity (logged in with pin)

        Returns:
            is_validated (bool)
        
        """
        return self._is_validated

    @property
    def accounts(self):
        """"Gets list of accounts

        Returns:
            accounts (list)
        
        """
        if self._is_validated == True:
            return self._accounts

    def logout(self):  # End session: used if data saved to database eventually
        """Calls destructor to end session"""
        self._is_validated = False
        del self
        
    def __init__(self):
        self.add("Homer Simpson", "1111111111", "1111", "111111111101,111111111102")
        self.add("Peter Griffin", "2222222222", "2222", "222222222201,222222222202")
        self.validate("1111111111", "1111")

    def add(self, name="", card_id="", pin="", accounts=""):
        customer = {
            "name": name,
            "card_id": card_id,
            "pin": pin,
            "accounts": accounts.replace(" ", "").split(",")
        }
        self._customers.append(customer)

    def validate(self, card_id, pin):
        """Validates whether card number and pin
        
        Args:
            card_id (string): customer card id number
            pin (string): customer pin

        Returns:
            True: if pin and card_id match account
            False: if pin and card_id do not match account
        """
        self._name = None
        self._card_id = None
        self._pin = None
        self._accounts = None
        self._is_validated = False

        for customer in self._customers:
            if card_id == customer["card_id"] and pin == customer["pin"]:
                self._name = customer["name"]
                self._card_id = card_id
                self._pin = pin
                self._accounts = customer["accounts"]
                self._is_validated = True
                return True

        return False

    def add_account(self, account_number):
        """Adds new account number to accounts
        
        Args:
            account_number (string): account number to be added to accounts

        Returns:
            True: if account number successfully added to accounts
            False: if session is not validated and account number not added
        
        """
        if self._is_validated == True:
            self._accounts.append(account_number)
            return True
        else:
            return False

if __name__ == "__main__":
    customer = Customer()
    print(customer.list)
