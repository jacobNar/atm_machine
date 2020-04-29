import tkinter as tk
from tkinter import font as tkfont
from tkinter import *


def numpad(value):
    global numbers

    numbers += value
    entry.insert('end', value)
    print(numbers)


keys = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    ['', '0', '.']
]
numbers = ''

root = tk.Tk()
root.title("ATM Number Pad")
entry = tk.Entry(root)
entry.grid(row=0, column=0, columnspan=3, ipady=5)
for y, row in enumerate(keys, 1):
    for x, key in enumerate(row):
        buttons = tk.Button(root, text=key, command=lambda val=key: numpad(val))
        buttons.grid(row=y, column=x, ipadx=10, ipady=10)

    b = Button(root, text="Enter", width=10, height=2)
    c = Button(root, text="Clear", width=10, height=2, command=entry.delete(0, END))
    b.grid(row=1, column=4, sticky=W)
    c.grid(row=2, column=4, sticky=W)
root.mainloop()


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MainPage, Deposit, Withdraw, Transfer, Account):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainPage")

    def show_frame(self, page_name):
        """Shows a frame for the given page name"""
        frame = self.frames[page_name]
        frame.tkraise()


class MainPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        button1 = tk.Button(self, text="Deposit", command=lambda: controller.show_frame("Deposit"))
        button2 = tk.Button(self, text="Withdraw", command=lambda: controller.show_frame("Withdraw"))
        button3 = tk.Button(self, text="Transfer", command=lambda: controller.show_frame("Transfer"))
        button4 = tk.Button(self, text="Account", command=lambda: controller.show_frame("Account"))
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()


class Deposit(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Deposit", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Return", command=lambda: controller.show_frame("MainPage"))
        button.pack()


class Withdraw(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Withdraw", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Return", command=lambda: controller.show_frame("MainPage"))
        button.pack()


class Transfer(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Transfer", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Return", command=lambda: controller.show_frame("MainPage"))
        button.pack()


class Account(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Account", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Return", command=lambda: controller.show_frame("MainPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()


