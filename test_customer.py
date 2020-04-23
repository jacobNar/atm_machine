import pytest
import customer

def test_init():
    _customer = customer.Customer()
    assert _customer != None

def test_name():
    _customer = customer.Customer()
    _customer.name = "Test"
    assert _customer.name == "Test"

def test_validate_card_id_pin():
    _customer = customer.Customer()
    customer._pin = '1111'
    customer._card_id = '1111'
    assert _customer.validate_card_id_pin('1111', '1111') == True

