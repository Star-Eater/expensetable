from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import ttk

count = 0

def add_record():

    global count

    try:
        plt.close()
    except:
        print('New Chart')


    my_tree.insert(parent='', index='end', iid=count, text='Parent', values=(Letter.get(), number_entry.get()))

    count += 1

    if Letter.get():
        if Letter.get() == 'A':
            try:
                smalldata.update(A = smalldata['A'] + int(number_entry.get()))
                print(smalldata)
            except:
                smalldata['A'] = (int(number_entry.get()))
        if Letter.get() == 'B':
            try:
                smalldata.update(B = smalldata['B'] + int(number_entry.get()))
                print(smalldata)
            except:
                smalldata['B'] = (int(number_entry.get()))
        if Letter.get() == 'C':
            try:
                smalldata.update(C = smalldata['C'] + int(number_entry.get()))
                print(smalldata)
            except:
                smalldata['C'] = (int(number_entry.get()))

    number_entry.delete(0, END)

    for k,v in smalldata.items():
        k = smalldata.keys()
        v = smalldata.values()

    figure2 = Figure(figsize=(4.2,4), dpi=100)
    subplot2 = figure2.add_subplot(111)

    subplot2.pie(v, labels=k)

    pie2 = FigureCanvasTkAgg(figure2, root)
    pie2.get_tk_widget().grid(column=0, row=4)



root = Tk()

smalldata = {}

Letter = StringVar()

dropmenu = OptionMenu(root, Letter, 'A', 'B', 'C')
dropmenu.grid(column=0, row=0)


il = Label( text='Number')
il.grid(row=0, column=1)


number_entry = Entry()
number_entry.grid(row=1, column=1)

add_Record = Button(root, text='Add Record', command = add_record)
add_Record.grid(column=2, row=1)

my_tree = ttk.Treeview()

my_tree['column'] = ('Letter', 'Number')

my_tree.column('#0', width=0)
my_tree.column('Letter', width=120)
my_tree.column('Number', width=120)

my_tree.heading('Letter', text='Letter')
my_tree.heading('Number', text='Number')

my_tree.grid(column=3, row=1)

root.mainloop()
