# Customer module to handle customer information

class Customer(object):
    def __init__(self, name, card_id, pin, account_number):
        self.name = name
        self.card_id = card_id
        self.pin = pin
        self.account_number = account_number
        print("Customer created")


    def validate_card_id_pin(self, card_id, pin):
        if card_id == self.card_id and pin == self.pin:
            return self.account_number

    def get_customer_info(self, card_id, pin, account_number):
        pass
