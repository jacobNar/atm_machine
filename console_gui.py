import tkinter as tk


def code(value):
    global numbers
    numbers += value
    entry.insert('end', value)
    print(numbers)


keys = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['.', '0']
]
numbers = ''

root = tk.Tk()
root.title("ATM Number Pad")
entry = tk.Entry(root)
entry.grid(row=0, column=0, columnspan=3, ipady=5)
for y, row in enumerate(keys, 1):
    for x, key in enumerate(row):
        buttons = tk.Button(root, text=key, command=lambda val=key: code(val))
        buttons.grid(row=y, column=x, ipadx=10, ipady=10)

root.mainloop()

