import pytest


import atm as atm_library

def test_init():
    atm = atm_library.Atm()
    assert atm != None

def test_id():
    atm = atm_library.Atm()
    assert atm.id != None

def test_display_welcome(capsys):
    atm = atm_library.Atm()
    atm.display_welcome()
    captured = capsys.readouterr()
    assert "Welcome" in captured.out

def test_balanace():
    atm = atm_library.Atm()
    atm.log_in("1111111111", "1111")

    assert atm.balance == 0

def test_deposit():
    atm = atm_library.Atm()
    atm.log_in("1111111111", "1111")

    atm.deposit(100)
    assert atm.balance == 100

