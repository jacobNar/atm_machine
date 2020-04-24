# Customer module to handle customer information such as name, card number, pin, and account number

class Customer(object):
    _name = None
    _card_id = None
    _pin = None
    _account_number = None
    _is_validated = False  #session control: logged in with card/pin

    @property
    def name(self):
        return self._name

    @property
    def is_validated(self):
        return self._is_validated

    @property
    def pin(self):
        return self._pin

    @name.setter
    def name(self, value):
        if self._is_validated == True:
            self._name = value

    @pin.setter
    def pin(self, value):
        if self._is_validated == True:
            self._pin = value

    def logout(self):  # End session: used if data saved to database eventually
        del self
        
    def __init__(self, name="", card_id="", pin="", account_number=""):
        self._name = name
        self._card_id = card_id
        self._pin = pin
        self._account_number = account_number
        print(f"Customer created. Welcome, {name}!")

    def validate_card_id_pin(self, card_id, pin):
        if card_id == self._card_id and pin == self._pin:
            self._is_validated = True
            return True
        else:
            return False
