import pytest
import customer

def test_init():
    _customer = customer.Customer()
    assert _customer != None

def test_name():
    _customer = customer.Customer()
    assert "Homer Simpson" in _customer.name

def test_accounts():
    _customer = customer.Customer()
    assert "111111111101" in _customer.accounts
    assert "111111111102" in _customer.accounts

def test_is_validated():
    _customer = customer.Customer()
    assert _customer.is_validated == True

# @pytest.mark.skip
# def test_name_can_be_changed_while_validated():
#     _customer = customer.Customer()
#     _customer._is_validated = True
#     _customer.name = "Test"
#     assert _customer.name == "Test"

# @pytest.mark.skip
# def test_name_cant_be_changed_while_unvalidated():
#     _customer = customer.Customer()
#     _customer._is_validated = False
#     _customer.name = "Test"
#     assert _customer.name == ""

def test_validate_true_on_correct_id_pin():
    _customer = customer.Customer()
    assert _customer.validate("1111111111", "1111") == True

def test_validate_false_on_incorrect_id_pin():
    _customer = customer.Customer()
    assert _customer.validate("1111111111", "2222") == False

# def test_add_account_adds_correctly():
#     _customer = customer.Customer()
#     _customer._is_validated = True
#     _customer._accounts = ['12345']
#     assert _customer.add_account('54321') == True

def test_add_adds_customer():
    _customer = customer.Customer()
    _customer.add("Moe Howard", "3333333333", "3333", "333333333301,333333333302")
    _customer.validate("3333333333", "3333")
    assert _customer.name == "Moe Howard"
    assert _customer._card_id == "3333333333"
    assert "333333333301" in _customer.accounts
    assert "333333333302" in _customer.accounts
    assert _customer.is_validated == True
