import pytest
import customer

if __name__ == "__main__":
    customer = customer.Customer()

def test_init():
    _customer = customer.Customer()
    assert _customer != None

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

