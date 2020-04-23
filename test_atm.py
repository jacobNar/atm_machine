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