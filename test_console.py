import console


def test_pin():
    input_values = [1234]

    def input(prompt=None):
        return input_values.pop()

    console.input = input
    assert console.pin() == None


def test_menu():
    input_values = [2]

    def input(prompt=None):
        return input_values.pop()

    console.input = input
    assert console.menu() == None
