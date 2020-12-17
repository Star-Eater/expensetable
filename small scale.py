from tkinter import ttk
from tkinter import *
from tkinter import Menu, ttk, Toplevel, Button, LabelFrame, Label, Entry, Radiobutton, END
import math

global count
count = 0
profit = 0

def add_record():
    global profit
    global count

    profit+=int(number_entry.get())

    simple.set([], 'Total', profit)


    simple.insert(parent='', index='end', iid=count, text='Parent', values=(letter_entry.get(), number_entry.get(), profit))
    count += 1

    #Clear the boxes
    letter_entry.delete(0, END)
    number_entry.delete(0, END)


root = Tk()

root.title('Simple Test')


simple = ttk.Treeview(root)


simple['columns'] = ('Letter', 'Number', 'Total')

simple.column('#0', width=0, stretch=20)
simple.column('Letter', anchor=W, width=120)
simple.column('Number', anchor=CENTER, width=80)
simple.column('Total', anchor=W, width=120)

simple.heading('#0')
simple.heading('Letter', text='Letter', anchor=W)
simple.heading('Number', text='Number', anchor=CENTER)
simple.heading('Total', text='Total', anchor=W)

simple.pack(pady=20)

add_frame = Frame(root)
add_frame.pack(pady=20)

nl = Label(add_frame, text='Letter')
nl.grid(row=0, column=0)

il = Label(add_frame, text='Number')
il.grid(row=0, column=1)



letter_entry = Entry(add_frame)
letter_entry.grid(row=1, column=0)

number_entry = Entry(add_frame)
number_entry.grid(row=1, column=1)


add_Record = Button(root, text='Add Record', command = add_record)
add_Record.pack()















root.mainloop()
