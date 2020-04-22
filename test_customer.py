import pytest
import customer

def test_init():
    _customer = customer.Customer()
    assert _customer != None

def test_name():
    _customer = customer.Customer()
    _customer.name = "Test"
    assert _customer.name == "Test"

def test_validate_card_id_pin(capsys):
    pass
