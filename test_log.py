import pytest
import log


ID_field = 95
entry = "try this"
error = "no"


def test_get_dictionary_valid():
    assert log.get_dictionary("Not a database name") == "Database missing."


def test_get_dictionary_invalid():
    with pytest.raises(AssertionError):
        log.get_dictionary(23)


def test_Log_valid():
    assert log.Log().save(ID_field, entry, error) == "Database found."


def test_execute_get_sql_valid():
    assert log.execute_sql("DELETE FROM Log WHERE IDField = 95;") == "Database found."
    assert log.execute_sql("INSERT INTO Log('IDField', DateTime, Text, Error) VALUES(50, 'someday and time', 'This is gonna show up', 'yes');") == "Database found."
    assert log.execute_sql("DELETE FROM Log WHERE IDField = 50;") == "Database found."
    assert log.execute_sql("Thisisn'tSQL!!!") == "Invalid SQL."


def test_execute_sql_invalid():
    with pytest.raises(AssertionError):
        log.execute_sql(13)

