from tkinter import Toplevel, LabelFrame, Frame, Label, Entry, Button, Radiobutton, IntVar
import expensetrackergui
from expensetrackerfunction import submit



def add_window():

    Frame = Toplevel()


    Frame.title('Another Window')

    Date_label = Label(Frame, text='Date:')
    Name_label = Label(Frame, text='Name:')
    Transaction_Label = Label(Frame, text='Transaction:')
    Category_Label = Label(Frame, text='Category:')
    Description_Label = Label(Frame, text='Description:')

    Date_label.grid(column=0, row=0)
    Name_label.grid(column=0, row=1)
    Transaction_Label.grid(column=0, row=2)
    Category_Label.grid(column=0, row=3)
    Description_Label.grid(column=0, row=4)

    Date_Entry = Entry(Frame)
    Name_Entry = Entry(Frame)
    Transaction_Label = Entry(Frame)
    Category_Label = Entry(Frame)
    Description_Label = Entry(Frame)

    Date_Entry.grid(column=1, row=0)
    Name_Entry.grid(column=1, row=1)
    Transaction_Label.grid(column=1, row=2)
    Category_Label.grid(column=1, row=3)
    Description_Label.grid(column=1, row=4)

    Submit = Button(Frame, text='Submit', command=submit)
    Submit.grid(column=1, row=5, pady=20)

    r = tk.IntVar()

    RadioLayer = LabelFrame(Frame)
    RadioLayer.grid(column=0, row=6)

    Operation = [('Income', 1), ('Expense', -1)]

    for text, mode in Operation:
        Radiobutton(RadioLayer, text=text, variable=r, value=mode).pack()

    Frame.geometry('250x250')
