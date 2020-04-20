import pytest

import atm as atm_library

def test_atm_init():
    atm = atm_library.Atm()
    assert atm != None
