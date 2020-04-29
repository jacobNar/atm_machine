# Customer module to handle customer information such as name, card number, pin, and account number

customers = [
    {
        "name": "Homer Simpson",
        "card_id": "1111111111",
        "pin": "1111",
        "accounts": [
            "111111111101"
            "111111111102"
        ]
    },
    {
        "name": "Peter Griffin",
        "card_id": "2222222222",
        "pin": "2222",
        "accounts": [
            "222222222201"
            "222222222202"
        ]
    },
]

class Customer(object):
    """Customer class for ATM

    Att: 
        name (string): customer first/last name
        card_id (string): customer card number
        pin (string): customer pin
        accounts (list): list of account numbers
        is_validated (bool): card number and pin validation/session

    """
    _name = None
    _card_id = None
    _pin = None
    _is_validated = False  #session control: logged in with card/pin
    _accounts = []

    @property
    def name(self):
        """name accessor function"""
        return self._name

    @property
    def is_validated(self):
        """Session validation accessor function"""
        return self._is_validated

    @property
    def accounts(self):
        """Name accessor function"""
        if self._is_validated == True:
            return self._accounts

    def logout(self):  # End session: used if data saved to database eventually
        """Calls destructor to end session"""
        _is_validated = False
        del self
        
    def __init__(self, name="", card_id="", pin="", accounts = []):
        """Customer constructor: name, card_id, pin, account_number"""
        self._name = name
        self._card_id = card_id
        self._pin = pin
        self._accounts = accounts
        # print(f"Customer created. Welcome, {name}!")

    def validate_card_id_pin(self, card_id, pin):
        """Validates whether card number and pin"""
        if card_id == self._card_id and pin == self._pin:
            self._is_validated = True
            return True
        else:
            self._is_validated = False
            return False

    def add_account(self, account_number):
        """Adds new account number to accounts"""
        if self._is_validated == True:
            self._accounts.append(account_number)
            return True
        else:
            return False

    # def get_account_number(self, card_id):
    #     """Gets account number if card_id and pin are validated"""
    #     if self._is_validated == True:
    #         return self._account_number

    # def get_accounts(self, card_id):
    #     """Gets accounts if card_id and pin are validated"""
    #     if self._is_validated == True:
    #         return self._accounts