import tkinter as tk
import account


def create_root():
    """Creates top-level window.

    Args: none
    
    Returns: none

    Modifies: global root
        
    """
    global root

    root = tk.Tk()
    root.title("Account")


def create_canvas():
    """Creates fixed size canvas.

    Args: none

    Returns: none

    """

    canvas = tk.Canvas(root, height=100, width=700)
    canvas.pack()


def create_button(button_name):
    """Creates a button.

    Args: none

    Returns: none

    """

    button = tk.Button(
        root, text=button_name, font=("Helvetica", 15),
        # command=lambda: account.balance
    )
    button.pack()


def create_entry():
    """Creates a one line entry field.

    Args: none

    Returns: none

    """

    entry = tk.Entry(root)
    entry.pack()
    print(entry)


def create_label(text_to_display):
    label = tk.Label(root, text = text_to_display)
    label.pack()


def main():
    """Runs the main program logic."""
    _account = account.Account()
    create_root()
    create_canvas()

    create_button("Get account balance!")

    create_label("Enter amount to deposit:")
    create_entry()
    create_button("Deposit!")

    create_label("Enter amount to withdraw:")
    create_entry()
    create_button("Withdraw!")

    root.mainloop()

if __name__ == "__main__":
    main()