import pytest
import log
from datetime import datetime


date_and_time = str(datetime.now())
date_and_time = date_and_time[0:19]
entry = "Description of changed aspect"
instance = {"Headings" : ["FieldID", "DateTime", "Text"], "Rows" : [["1", date_and_time, "Description of changed aspect"]]}
instance_with_columns = {"Column Widths" : [9, 21, 31], "Headings" : ["FieldID", "DateTime", "Text"], "Rows" : [["1", date_and_time, "Description of changed aspect"]]}


def test_get_dictionary_valid():
    assert log.get_dictionary("Not a database name") == "Database empty."


def test_get_dictionary_invalid():
    with pytest.raises(AssertionError):
        log.get_dictionary(23)


def test_Log_valid():
    assert log.Log().show() == "Database empty."
    assert log.Log().save(entry) == "Database found."
    assert log.Log().show() == " \tFieldID  DateTime             Text                           \n1:      1        " + date_and_time + "  Description of changed aspect  \n"


def test_attach_column_widths_valid():
    assert log.attach_column_widths(instance) == instance_with_columns
    dictionary = {"Headings" : ["FieldID", "DateTime", "Text"], "Rows" : [["1", date_and_time, "Description of changed aspect"]]}
    dictionary_with_columns = {"Column Widths" : [9, 21, 31], "Headings" : ["FieldID", "DateTime", "Text"], "Rows" : [["1", date_and_time, "Description of changed aspect"]]}
    assert log.attach_column_widths(dictionary) == dictionary_with_columns 


def test_attach_column_widths_invalid():
    not_a_dictionary = ["random", "list"]
    with pytest.raises(AssertionError):
        log.attach_column_widths(not_a_dictionary)
    dictionary_without_heading_lists = {"Headings" : 3}
    with pytest.raises(AssertionError):
        log.attach_column_widths(dictionary_without_heading_lists)
    dictionary_without_row_lists = {"Headings" : ["FieldID", "DateTime", "Text"], "Rows" : 5}
    with pytest.raises(AssertionError):
        log.attach_column_widths(dictionary_without_row_lists)
    not_a_list_of_lists = {"Headings" : ["FieldID", "DateTime", "Text"], "Rows" : [5, 3]}
    with pytest.raises(AssertionError):
        log.attach_column_widths(not_a_list_of_lists)
    not_the_same_length = {"Headings" : ["FieldID", "DateTime", "Text"], "Rows" : [["apples", "bananas", "hold up", "FOURTH THING THAT'S NOT SUPPOSED TO BE HERE"], ["whoa", "this"], ["is", "hard"]]}
    with pytest.raises(AssertionError):
        log.attach_column_widths(not_the_same_length)


def test_return_table_valid():
    assert log.return_table(instance) == " \tFieldID  DateTime             Text                           \n1:      1        " + date_and_time + "  Description of changed aspect  \n"


def test_return_table_invalid():
    not_a_dictionary = ["random", "list"]
    with pytest.raises(AssertionError):
        log.return_table(not_a_dictionary)
    dictionary_without_heading_lists = {"Headings" : 3}
    with pytest.raises(AssertionError):
        log.return_table(dictionary_without_heading_lists)
    dictionary_without_row_lists = {"Headings" : ["FieldID", "DateTime", "Text"], "Rows" : 5}
    with pytest.raises(AssertionError):
        log.return_table(dictionary_without_row_lists)
    not_a_list_of_lists = {"Headings" : ["FieldID", "DateTime", "Text"], "Rows" : [5, 3]}
    with pytest.raises(AssertionError):
        log.return_table(not_a_list_of_lists)
    not_the_same_length = {"Headings" : ["FieldID", "DateTime", "Text"], "Rows" : [["apples", "bananas", "cherries", "4TH THING THAT'S NOT SUPPOSED TO BE HERE"]]}
    with pytest.raises(AssertionError):
        log.return_table(not_the_same_length)


def test_execute_get_sql_valid():
    assert log.execute_sql("DELETE FROM Log WHERE Text = 'Description of changed aspect';") == "Database found."
    assert log.execute_sql("INSERT INTO Log('FieldID', DateTime, Text) VALUES(50000000000, '4/22/2020', 'This is gonna show up');") == "Database found."
    assert log.execute_sql("DELETE FROM Log WHERE FieldID = '50000000000';") == "Database found."
    assert log.execute_sql("Thisisn'tSQL!!!") == "Invalid SQL."


def test_execute_sql_invalid():
    with pytest.raises(AssertionError):
        log.execute_sql(13)
