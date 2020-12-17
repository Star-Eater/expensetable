import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import *
from tkinter import Menu, ttk, Toplevel, Button, LabelFrame, Label, Entry, Radiobutton, END


root = tk.Tk()

root.title('Small Scale Pie Chart')




global count
count = 0
profit = 0

piedata  = {'Income': 0, 'Food': 0, 'Utility': 0, 'Subscriptions': 0}




def add_record():
    global profit
    global count



    if Category.get():


        profit+=int(number_entry.get())

        simple.set([], 'Total', profit)

        simple.insert(parent='', index='end', iid=count, text='Parent', values=(letter_entry.get(), number_entry.get(), Category.get(), profit))
        count += 1

        if Category.get() == 'Income':
            piedata.update(Income = piedata['Income'] + int(number_entry.get()) )

        if Category.get() == 'Food':
            piedata.update(Income = piedata['Food'] + int(number_entry.get()) )

        if Category.get() == 'Utility':
            piedata.update(Income = piedata['Utility'] + int(number_entry.get()) )

        if Category.get() == 'Subscriptions':
            piedata.update(Income = piedata['Subscriptions'] + int(number_entry.get()) )

        #Clear the boxes
        letter_entry.delete(0, END)
        number_entry.delete(0, END)

        for k,v in piedata.items():
            k = piedata.keys()
            v = piedata.values()

        figure2 = Figure(figsize=(4.2,4), dpi=100)
        subplot2 = figure2.add_subplot(111)

        subplot2.pie(v, labels=k)

        pie2 = FigureCanvasTkAgg(figure2, root)
        pie2.get_tk_widget().grid(column=0, row=4)


    else:
        print('Select a Category')


simple = ttk.Treeview(root)


simple['columns'] = ('Letter', 'Number', 'Category', 'Total')

simple.column('#0', width=0, stretch=20)
simple.column('Letter', anchor=W, width=120)
simple.column('Number', anchor=CENTER, width=80)
simple.column('Category', anchor=CENTER, width=120)
simple.column('Total', anchor=W, width=120)

simple.heading('#0')
simple.heading('Letter', text='Letter', anchor=W)
simple.heading('Number', text='Number', anchor=CENTER)
simple.heading('Category', text='Category', anchor=CENTER)
simple.heading('Total', text='Total', anchor=W)

simple.grid(column=0, row=0, pady=20)

add_frame = Frame(root)
add_frame.grid(column=1, row=1)

nl = Label(add_frame, text='Letter')
nl.grid(row=0, column=0)

il = Label(add_frame, text='Number')
il.grid(row=0, column=1)



letter_entry = Entry(add_frame)
letter_entry.grid(row=1, column=0)

number_entry = Entry(add_frame)
number_entry.grid(row=1, column=1)


add_Record = Button(root, text='Add Record', command = add_record)
add_Record.grid(column=2, row=2)


Category = StringVar()


dropmenu = OptionMenu(root, Category, 'Income', 'Food', 'Utility', 'Subscriptions')
dropmenu.grid(column=0, row=1)






root.mainloop()
