# Customer module to handle customer information such as name, card number, pin, and account number

class Customer(object):
    """Customer class for ATM

    Att: 
        name (string): customer first/last name
        card_id (string): customer card number
        pin (string): customer pin
        account_number (string): account number
        is_validated (bool): card number and pin validation/session

    """
    _name = None
    _card_id = None
    _pin = None
    _account_number = None
    _is_validated = False  #session control: logged in with card/pin
    _accounts = []

    @property
    def name(self):
        """name accessor function"""
        return self._name

    @property
    def is_validated(self):
        """is_validated accessor function"""
        return self._is_validated

    # @property
    # def pin(self):
    #     """pin accessor function"""
    #     if self._is_validated == True:
    #         return self._pin

    # @name.setter
    # def name(self, value):
    #     """name accessor function"""
    #     if self._is_validated == True:
    #         self._name = value

    # @pin.setter
    # def pin(self, value):
    #     """pin mutator function"""
    #     if self._is_validated == True:
    #         self._pin = value

    def logout(self):  # End session: used if data saved to database eventually
        """Calls destructor to end session"""
        _is_validated = False
        del self
        
    def __init__(self, name="", card_id="", pin="", account_number="", accounts = []):
        """Customer constructor: name, card_id, pin, account_number"""
        self._name = name
        self._card_id = card_id
        self._pin = pin
        self._account_number = account_number
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

    
    def get_accounts(self, _is_validated, accounts)
        if self._is_validated == True:
            return accounts
