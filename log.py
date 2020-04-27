import sqlite3
from datetime import datetime


DATABASE = "Log.db"


class Log(object):

    def save(self, entry):
        """Saves a string to a database with an incrementing ID and a datetime.

        Args:
            entry: The string to be saved to the database.

        Returns:
            Either 'Database found.' or 'Database missing.' depending on the result.

        Raises:
            AssertionError: If the entry text is not a string.
        """
        assert isinstance(entry, str), "The Log text should be a string."
        fieldID = get_dictionary("SELECT COUNT(*) FROM Log")
        fieldID = int(fieldID["Rows"][0][0])
        fieldID += 1
        date_and_time = datetime.now()
        sql = "INSERT INTO Log('FieldID', DateTime, Text) VALUES('"
        sql = sql + str(fieldID) + "', '" + str(date_and_time) + "', '" + str(entry) + "');"
        results = execute_sql(sql)
        return results
    
    
    def display_entry(self):
        """Displays all the records of the log.

        Args:
            None

        Returns:
            None
        """
        sql = "SELECT * from Log"
        list_of_dictionaries = get_dictionary(sql)
        print("\nThe log entries are:\n")
        display_table(list_of_dictionaries)


def execute_sql(sql):
    """Executes the given sql statement.

    Args:
        sql: A valid SQL statement to execute.

    Returns:
        Either 'Database found.' or 'Invalid SQL.' depending on whether the database was accessed.

    Raises:
        AssertionError: If SQL is not a string.
    """
    assert(isinstance(sql, str)), "SQL must be a string."
    result = ""
    try:
        connection = sqlite3.connect(DATABASE)
    except:
        print(f"Unable to connect to {DATABASE}")
        raise

    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        print("Change successful.")
        result = "Database found."
    except Exception as exception:
        print(f"Unable to execute {sql}")
        print(exception)
        result = "Invalid SQL."
    finally:
        connection.close()
    return result


def get_dictionary(sql):
    """Executes the SQL code in a database and returns the headings and rows in a dictionary of lists.
    
    Args:
        sql: The SQL code to be executed.

    Returns:
        A dictionary of lists 
    
    Raises:
        AssertionError: If sql is not a string.
    """
    assert isinstance(sql, str), "'sql' must be a string."
    dictionary = {}
    column_headings = []
    rows_contents = []

    connection = sqlite3.connect(DATABASE)
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        
        loop_count = 0
        column_names = cursor.description
        while loop_count < len(column_names):
            column_name = column_names[loop_count][0]
            column_headings.append(column_name)
            loop_count += 1
        dictionary["Headings"] = column_headings

        loop_count = 0
        rows = cursor.fetchall()
        if rows != []:
            while loop_count < len(rows):
                small_loop = 0
                small_row = []
                while small_loop < len(dictionary["Headings"]):
                    row = str(rows[loop_count][small_loop])
                    small_row.append(row)
                    small_loop += 1
                rows_contents.append(small_row)
                loop_count += 1
            dictionary["Rows"] = rows_contents
        else:
            dictionary = "Database missing."
    except Exception as exception:
            print("Error processing %s" % sql)
            print(exception)
    finally:
        connection.close()
    if dictionary == {}:
        dictionary = "Database missing."
    return dictionary


def attach_column_widths(dictionary_of_lists):
    """Finds and attaches a list of the column widths to the dictionary.
    
    Args:
        dictionary_of_lists: A dictionary of lists made from the database.
        answer: The table selected by the user.
    
    Returns:
        The dictionary of lists with an extra entry with the column widths.

    Raises:
        AssertionError: If dictionary_of_lists is not a dictionary.
        AssertionError: If 'Heading' key does not access a list.
        AssertionError: If 'Rows' key does not access a list.
        AssertionError: If 'Rows' key does not access a list of lists.
        AssertionError: If the length of headings and number of values in row are not equal.
    """
    assert isinstance(dictionary_of_lists, dict), "'dictionary_of_lists ' must be a dictionary."
    assert isinstance(dictionary_of_lists["Headings"], list), "'Headings' key should access a list."
    assert isinstance(dictionary_of_lists["Rows"], list), "'Rows' key should access a list."
    assert isinstance(dictionary_of_lists["Rows"][0], list), "'Rows' key should access a list of lists."
    assert len(dictionary_of_lists["Headings"]) == len(dictionary_of_lists["Rows"][0]), "Length of headings should equal the number of values in a rows."
    loop_count = 0
    list_of_column_widths = []
    while loop_count < len(dictionary_of_lists["Headings"]):
        instance_heading = dictionary_of_lists["Headings"][loop_count]
        sql = "SELECT MAX(LENGTH(" + str(instance_heading) + ")) FROM Log"
        sql_result = get_dictionary(sql)
        column_width = int(sql_result["Rows"][0][0]) + 2
        if column_width > 40:
            column_width = 40
        if len(instance_heading) + 2 < column_width:
            list_of_column_widths.append(column_width)
        else:
            list_of_column_widths.append(len(instance_heading) + 2)
        loop_count += 1
    dictionary_of_lists["Column Widths"] = list_of_column_widths
    return dictionary_of_lists


def display_table(dictionary_of_lists):
    """Prints the information from the dictionary in a table.
    
    Args:
        dictionary_of_lists: A dictionary of lists made from the database.
        answer: The table selected by the user.
    
    Returns:
        The dictionary of lists with an extra entry with the column widths.

    Raises:
        AssertionError: If dictionary_of_lists is not a dictionary.
        AssertionError: If 'Heading' key does not access a list.
        AssertionError: If 'Rows' key does not access a list.
        AssertionError: If 'Rows' key does not access a list of lists.
        AssertionError: If the length of headings and number of values in row are not equal.
        AssertionError: If 'Column Widths' key does not access a list.
        AssertionError: If 'Column Widths' key does not access a list of integers.
    """
    assert isinstance(dictionary_of_lists, dict), "'dictionary_of_lists ' must be a dictionary."
    assert isinstance(dictionary_of_lists["Headings"], list), "'Headings' key should access a list."
    assert isinstance(dictionary_of_lists["Rows"], list), "'Rows' key should access a list."
    assert isinstance(dictionary_of_lists["Rows"][0], list), "'Rows' key should access a list of lists."
    assert len(dictionary_of_lists["Headings"]) == len(dictionary_of_lists["Rows"][0]), "Length of headings should equal the number of values in a rows."
    loop_count = 0
    top_row = " \t"
    dictionary_of_lists = attach_column_widths(dictionary_of_lists)
    assert isinstance(dictionary_of_lists["Column Widths"], list), "'Column Widths' key should access a list."
    assert isinstance(dictionary_of_lists["Column Widths"][0], int), "'Column Widths' key should access a list of integers."
    while loop_count < len(dictionary_of_lists["Headings"]):
        instance_heading = str(dictionary_of_lists["Headings"][loop_count])
        instance_column_width = int(dictionary_of_lists["Column Widths"][loop_count])
        top_row += f"{instance_heading:{instance_column_width}}"
        loop_count += 1
    print(top_row)

    loop_count = 0
    while loop_count < len(dictionary_of_lists["Rows"]):
        row_count = str(loop_count + 1) + ":"
        row = f"{row_count:{8}}"
        small_loop = 0
        while small_loop < len(dictionary_of_lists["Rows"][loop_count]):
            instance_row = str(dictionary_of_lists["Rows"][loop_count][small_loop])
            if len(instance_row) > 38:
                instance_row = instance_row[0:37] + "..."
            instance_column_width = int(dictionary_of_lists["Column Widths"][small_loop])
            row += f"{instance_row:{instance_column_width}}"
            small_loop += 1
        print(row)
        loop_count += 1
    return loop_count


if __name__ == "__main__":
    entry = "Description of changed aspect"
    Log().save(entry)
    Log().display_entry()