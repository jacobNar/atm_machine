import sqlite3

DATABASE = "Log.db"

class Log(object):

    def save(self, ID_number, entry):
        assert isinstance(ID_number, int), "Credit card/Account number should be an integer."
        assert isinstance(entry, str), "The Log text should be a string."
        sql = "INSERT INTO Log(IDNumber, LogText) VALUES("
        sql = sql + str(ID_number) + ", " + str(entry) + ");"
        results = execute_sql(sql)
        return results


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

if __name__ == "__main__":
    # Credit card number or Account number perhaps?
    ID_number = 1234123412341234

    # The thing that was accessed or changed.
    entry = "Description of changed aspect"

    Log().save(ID_number, entry)