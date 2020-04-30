import console as console_library


def test_init():
    console = console_library.Console()
    assert console is not None


def test_get_pin():
    console = console_library.Console()
    input_values = ["1111"]

    def input(prompt=None):
        return input_values.pop()

    console_library.input = input
    assert console.get_pin() == "1111"


def test_invalid_pin_over_four_digits_prints_string(capsys):
    console = console_library.Console()
    input_values = ["999999", "9999"]

    def input(prompt=None):
        return input_values.pop(0)

    console_library.input = input
    assert console.get_pin() == "9999"

    captured = capsys.readouterr()
    assert "Invalid PIN" in captured.out


def test_invalid_pin_under_four_digits_prints_string(capsys):
    console = console_library.Console()
    input_values = ["1", "1111"]

    def input(prompt=None):
        return input_values.pop(0)

    console_library.input = input
    assert console.get_pin() == "1111"

    captured = capsys.readouterr()
    assert "Invalid PIN" in captured.out


def test_get_card():
    console = console_library.Console()
    input_values = ["123412341234"]

    def input(prompt=None):
        return input_values.pop()

    console_library.input = input
    assert console.get_card() == "123412341234"


def test_get_card_string(capsys):
    console = console_library.Console()
    input_values = ["123412341234"]

    def input(prompt=None):
        return input_values.pop()

    console_library.input = input
    assert console.get_card() == "123412341234"
    captured = capsys.readouterr()
    assert "Valid card ID!" in captured.out 


def test_console_display_menu_prints_string(capsys):
    console = console_library.Console()
    input_values = ["1", "100", "Y"]

    def input(prompt=None):
        return input_values.pop(0)

    console_library.input = input
    assert console.display_menu() == "1"

    captured = capsys.readouterr()
    assert "Deposit verified!" in captured.out
