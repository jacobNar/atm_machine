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
        
    def __init__(self, name="", card_id="", pin="", accounts = []):
        """Customer constructor: name, card_id, pin, accounts
            name (string)
            card_id (string)
            pin (string)
            accounts (list of strings)
        """
        self._name = name
        self._card_id = card_id
        self._pin = pin
        self._accounts = accounts

    def validate_card_id_pin(self, card_id, pin):
        """Validates whether card number and pin
        
        Args:
            card_id (string): customer card id number
            pin (string): customer pin

        Returns:
            True: if pin and card_id match account
            False: if pin and card_id do not match account
        """
        if card_id == self._card_id and pin == self._pin:
            self._is_validated = True
            return True
        else:
            self._is_validated = False
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
