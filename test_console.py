import console as console_library


def test_init():
    console = console_library.Console(1111, 1, 0, 1)
    assert console is not None


def test_get_pin():
    input_values = [1111]

    def input(prompt=None):
        return input_values.pop()

    console_library.input = input
    assert console_library.get_pin() == 1111


def test_invalid_pin_over_four_digits():
    input_values = [999999]

    def input(prompt=None):
        return input_values.pop()

    console_library.input = input
    assert console_library.get_pin() is None


def test_invalid_pin_under_four_digits():
    input_values = [1]

    def input(prompt=None):
        return input_values.pop()

    console_library.input = input
    assert console_library.get_pin() is None


def test_get_choice():
    input_values = [1]

    def input(prompt=None):
        return input_values.pop()

    console_library.input = input
    assert console_library.get_choice() == 1



