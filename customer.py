# Customer module to handle customer information

class Customer(object):
    _name = None
    _card_id = None
    _pin = None
    _account_number = None

    def __init__(self, name, card_id, pin, account_number):
        self._name = name
        self._card_id = card_id
        self._pin = pin
        self._account_number = account_number
        print("Customer created")


    def validate_card_id_pin(self, card_id, pin):
        if card_id == self._card_id and pin == self._pin:
            return self.account_number # or return True if validated?
            

    def get_customer_info(self, name, card_id, pin, account_number):
        pass
