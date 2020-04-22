import pytest
import log


FieldID = 95
entry = "try this"


def test_get_dictionary_valid():
    assert log.get_dictionary("Not a database name") == "Database missing."


def test_get_dictionary_invalid():
    with pytest.raises(AssertionError):
        log.get_dictionary(23)


def test_Log_valid():
    assert log.Log().save(FieldID, entry) == "Database found."


def test_execute_get_sql_valid():
    assert log.execute_sql("DELETE FROM Log WHERE FieldID = 95;") == "Database found."
    assert log.execute_sql("INSERT INTO Log('FieldID', DateTime, Text) VALUES(50, 'someday and time', 'This is gonna show up');") == "Database found."
    assert log.execute_sql("DELETE FROM Log WHERE FieldID = 50;") == "Database found."
    assert log.execute_sql("Thisisn'tSQL!!!") == "Invalid SQL."


def test_execute_sql_invalid():
    with pytest.raises(AssertionError):
        log.execute_sql(13)

