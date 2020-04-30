# Creates a customer form gui for entry of a 
# new customer using the customer module

import tkinter
from tkinter import messagebox
import customer


root = None
scrolledtext = None


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

    root = tkinter.Tk()
    root.title("Welcom to New Customer Registration")


def create_canvas():
    """Creates fixed size canvas.

    Args:
        None

    Returns:
        None

    """

    canvas = tkinter.Canvas(root, height=500, width=500, bg='#DFE3E5')
    canvas.pack()


def create_label(text, rel_x, rel_y, rel_height, rel_width, b_g):
    """Creates labels.

    Args:
        text (string): text to display
        rel_x (float): relative x location
        rel_y (float): relative y location
        rel_height (float): relative height
        rel_width (float): relative width
        b_g (string): hexadecimal background color

    Returns:
        None

    """
    label = tkinter.Label(root, text = text, font=("Helvetica", 16), bg=b_g)
    label.place(relx=rel_x, rely=rel_y, relheight=rel_height, relwidth=rel_width)


def create_submit_button(name, card_id, pin, accounts):
    """Creates text - print button.

    Args:
        name, card_id, pin, accounts text fields

    Returns:
        None

    """

    button = tkinter.Button(
        root, text="Submit New Customer", font=("Helvetica", 12), bg='#ABADAF',
        command=lambda : submit_customer_info(name, card_id, pin, accounts))
    
    button.place(relx=0.33, rely=0.8, relheight=0.1, relwidth=0.35)


def create_entry(rel_x, rel_y, rel_height, rel_width):
    """Creates a one line entry field.

    Args: 
        rel_x (float): relative x location
        rel_y (float): relative y location
        rel_height (float): relative height
        rel_width (float): relative width
        b_g (string): hexadecimal background color

    Returns: entry field

    """

    entry = tkinter.Entry(root, font=("Helvetica", 12),)
    entry.place(relx=rel_x, rely=rel_y, relheight=rel_height, relwidth=rel_width)
    return entry


def submit_customer_info(name, card_id, pin, accounts):
    """Gets customer form data from Entry fields and 
        creates customer using customer module.

    Args: name, card_id, pin, accounts text fields

    Returns: none

    """
    keys = ["name", "card_id", "pin", "accounts"]
    elements = [name.get(), card_id.get(), pin.get(), accounts.get()]
    custdict = dict(zip(keys, elements))
    #print(custdict)
    customer.Customer.add(custdict)
    tkinter.messagebox.showinfo(title="Notification", message="Customer Successfully Registered!")


def main():
    """Runs the main program logic."""
    create_root()
    create_canvas()

    create_label("Customer Registration Form", 0, 0, 0.1, 1, '#ABADAF')
    create_label("Full Name", 0.05, 0.2, 0.05, 0.30, '#DFE3E5')
    create_label("Card ID Number", 0.05, 0.35, 0.05, 0.3, '#DFE3E5')
    create_label("Pin", 0.05, 0.5, 0.05, 0.3, '#DFE3E5')
    create_label("Accounts", 0.05, 0.65, 0.05, 0.3, '#DFE3E5')

    name = create_entry(0.450, 0.2, 0.05, 0.45)
    card_id = create_entry(0.450, 0.35, 0.05, 0.45)
    pin = create_entry(0.450, 0.5, 0.05, 0.45)
    accounts = create_entry(0.450, 0.65, 0.05, 0.45)

    create_submit_button(name, card_id, pin, accounts)
    root.mainloop()
    
if __name__ == "__main__":
    main()
