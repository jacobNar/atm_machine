import pytest
import log


ID_number = 95
entry = "'thry this'"


def test_Log_valid():
    assert log.Log().save(ID_number, entry) == "Database found."



def test_execute_get_sql_valid():
    assert log.execute_sql("INSERT INTO Log(IDNumber, LogText) VALUES(50, 'This is gonna show up');") == "Database found."
    assert log.execute_sql("DELETE FROM Log WHERE IDNumber = 50;") == "Database found."
    assert log.execute_sql("Thisisn'tSQL!!!") == "Invalid SQL."


def test_execute_sql_invalid():
    with pytest.raises(AssertionError):
        log.execute_sql(13)
