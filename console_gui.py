import tkinter as tk
from tkinter import *

keys = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    ['←', '0', '.']
]
numbers = ''

root = tk.Tk()
root.title("Console")

deposit = Frame(root)
withdraw = Frame(root)
transfer = Frame(root)
account = Frame(root)

entry = tk.Entry(root)
entry.grid(row=0, column=0, columnspan=3, ipady=5)
for y, row in enumerate(keys, 1):
    for x, key in enumerate(row):
        buttons = tk.Button(root, text=key, command=lambda val=key: numpad(val))
        buttons.grid(row=y, column=x, ipadx=10, ipady=10)

    for frame in (deposit, withdraw, transfer, account):
        frame.grid(row=0, column=0)
    button1 = tk.Button(root, text="Deposit", command=lambda: deposit())
    button2 = tk.Button(root, text="Withdraw", command=lambda: withdraw())
    button3 = tk.Button(root, text="Transfer", command=lambda: transfer())
    button4 = tk.Button(root, text="Account", command=lambda: account())
    button1.grid(row=1, column=4)
    button2.grid(row=2, column=4)
    button3.grid(row=3, column=4)
    button4.grid(row=4, column=4)


def numpad(value):
    global numbers
    if value == '←':
        numbers = numbers[:-1]
        entry.delete('0', 'end')
        entry.insert('end', numbers)
    else:
        numbers += value
        entry.insert('end', value)
        print(numbers)


def enter_id():
    window = Tk()
    Label(window, text="Enter card ID: ").grid(row=0, column=1)
    e1 = Entry(window)
    e1.grid(row=1, column=0, columnspan=3, ipady=5)
    window.mainloop()


def enter_pin():
    window = Tk()
    Label(window, text="Enter PIN: ").grid(row=0, column=1)
    e1 = Entry(window)
    e1.grid(row=1, column=0, columnspan=3, ipady=5)
    window.mainloop()


def deposit():
    window = tk.Tk()
    window.title("Deposit")
    Label(window, text="Enter amount to deposit: ").grid(row=0, column=1)
    e1 = Entry(window)
    e1.grid(row=1, column=0, columnspan=3, ipady=5)
    button_deposit = Button(window, text="Submit")
    button_deposit.grid(row=2, column=1)
    window.mainloop()


def withdraw():
    window = tk.Tk()
    window.title("Withdraw")
    Label(window, text="Enter amount to withdraw: ").grid(row=0, column=1)
    e1 = Entry(window)
    e1.grid(row=1, column=0, columnspan=3, ipady=5)
    button_withdraw = Button(window, text="Submit")
    button_withdraw.grid(row=2, column=1)
    window.mainloop()


def transfer():
    window = tk.Tk()
    window.title("Transfer")
    Label(window, text="Enter amount to transfer: ").grid(row=0, column=1)
    e1 = Entry(window)
    e1.grid(row=1, column=0, columnspan=3, ipady=5)
    button_transfer = Button(window, text="Submit")
    button_transfer.grid(row=2, column=1)
    window.mainloop()


def account():
    window = tk.Tk()
    window.title("Account")
    label = tk.Label(window, text="Account", font=('Helvetica', 18), pady=10)
    label.grid(pady=10)
    window.mainloop()


root.mainloop()
