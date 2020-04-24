import console as console_library


def test_init():
    console = console_library.Console(1111, 1, 0)
    assert console is not None


def test_console_get_pin():
    input_values = [1111]

    def input(prompt=None):
        return input_values.pop()

    console_library.input = input
    assert console_library.Console.console_get_pin() == 1111


def test_invalid_pin_over_four_digits_prints_string(capsys):
    input_values = [999999]

    def input(prompt=None):
        return input_values.pop()

    console_library.Console.input = input
    captured = capsys.readouterr()
    assert captured.out == ""


def test_invalid_pin_under_four_digits_prints_string(capsys):
    input_values = [1]

    def input(prompt=None):
        return input_values.pop()

    console_library.Console.input = input
    captured = capsys.readouterr()
    assert captured.out == ""


def test_console_card_identification():
    input_values = [123412341234]

    def input(prompt=None):
        return input_values.pop()

    console_library.input = input
    assert console_library.Console.console_get_card_identification() == 123412341234


def test_console_card_identification_string(capsys):
    input_values = [123412341234]

    def input(prompt=None):
        return input_values.pop()

    console_library.input = input
    console_library.Console.console_get_card_identification()
    captured = capsys.readouterr()
    assert captured.out != "Valid card ID!"


def test_console_display_menu_prints_string(capsys):
    input_values = [1]

    def input():
        return input_values.pop()

    console_library.Console.input = input
    captured = capsys.readouterr()
    assert captured.out == ""


