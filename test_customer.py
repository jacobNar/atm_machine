import pytest
import customer

if __name__ == "__main__":
    customer = customer.Customer()

def test_init():
    _customer = customer.Customer()
    assert _customer != None

def test_name():
    _customer = customer.Customer()
    _customer.name = "name"
    assert _customer.name == "name"

def test_accounts():
    _customer = customer.Customer()
    _customer.accounts = ['12345', '12345']
    assert _customer.accounts == ['12345', '12345']

def test_is_validated():
    _customer = customer.Customer()
    _customer.is_validated = True
    assert _customer.is_validated == True

@pytest.mark.skip
def test_name_can_be_changed_while_validated():
    _customer = customer.Customer()
    _customer._is_validated = True
    _customer.name = "Test"
    assert _customer.name == "Test"

@pytest.mark.skip
def test_name_cant_be_changed_while_unvalidated():
    _customer = customer.Customer()
    _customer._is_validated = False
    _customer.name = "Test"
    assert _customer.name == ""

def test_validate_card_id_pin_true_on_correct_id_pin():
    _customer = customer.Customer()
    _customer._pin = 1111
    _customer._card_id = 1111
    assert _customer.validate_card_id_pin(1111, 1111) == True

def test_validate_card_id_pin_false_on_incorrect_id_pin():
    _customer = customer.Customer()
    _customer._pin = 1112
    _customer._card_id = 1111
    assert _customer.validate_card_id_pin(1111, 1111) == False

def test_add_account_adds_correctly():
    _customer = customer.Customer()
    _customer._is_validated = True
    _customer._accounts = ['12345']
    assert _customer.add_account('54321') == True


