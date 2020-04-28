"""
This program demonstrates Python GUI using tkinter.

Input:
    None

Output:
    None

Global variables:
    root (tkinter.root): top-level window
    text_table tkinter.Text: prints Hello World.

References:
    https://www.tutorialspoint.com/python/python_gui_programming.htm
    https://www.python-course.eu/python_tkinter.php
    https://wiki.python.org/moin/EscapingHtml

"""


from tkinter import *

root = None
text_table = None


def create_root():
    """Creates top-level window.

    Args:
        None

    Returns:
        None

    Modifies:
        global root

    """

    global root

    root = Tk()
    root.title("Example")


def create_canvas():
    """Creates fixed size canvas.

    Args:
        None

    Returns:
        None

    """

    canvas = Canvas(root, height=100, width=300)
    canvas.pack()


def create_button_print():
    """Creates text - print button.

    Args:
        None

    Returns:
        None

    """

    button = Button(
        root, text="Print Hello World !!!", font=("Helvetica", 8),
        command=lambda: display_text()
    )
    button.place(relx=0.07, rely=0.1, relheight=0.2, relwidth=0.35)


def create_button_clear():
    """Creates text - clear button.

    Args:
        None

    Returns:
        None

    """

    button_clear = Button(
        root, text="Clear Screen", font=("Helvetica", 8),
        command=lambda: text_table.destroy()
    )
    button_clear.place(relx=0.62, rely=0.1, relheight=0.2, relwidth=0.3)


def create_exit_button():
    """Creates exit button.

    Args:
        None

    Returns:
        None

    """
    button = Button(
        root, text="Exit", font=("Helvetica", 8), command=root.destroy
    )
    button.place(relx=0.72, rely=0.65, relheight=0.2, relwidth=0.2)


def display_text():
    """Creates text table..

    Args:
        None

    Returns:
        None

    Modifies:
        global text_table

    """

    global text_table
    text_table = Text(root, font=("Helvetica", 12), fg='blue', bd=5)
    text_table.insert(END, "Hello World !!!")
    text_table.pack(side=RIGHT)
    text_table.place(relx=0.08, rely=0.6, relwidth=0.38, relheight=0.30)


def main():
    """Main function of the program"""

    create_root()
    create_canvas()
    create_button_print()
    create_button_clear()
    create_exit_button()
    root.mainloop()


if __name__ == "__main__":
    main()