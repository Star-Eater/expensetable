import tkinter as tk
from tkinter import Menu, ttk, Toplevel, Button, LabelFrame, Label, Entry, Radiobutton, END, Frame, StringVar, OptionMenu
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import psycopg2


conn = psycopg2.connect(host='localhost', port=5433, dbname='postgres', user='postgres', password='slugger123')

#Create Database
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS expensetable
    (
    id SERIAL,
    Date TEXT NOT NULL,
    Name TEXT NOT NULL,
    Transaction TEXT NOT NULL,
    Category TEXT NOT NULL,
    Description TEXT NOT NULL,
    Total TEXT NOT NULL
    )
    """)

conn.commit()





#Create Gui
class MainApp(tk.Tk):

    def __init__(self, *args, **kwargs):


        tk.Tk.__init__(self, *args, *kwargs)

        container = tk.Frame(self)

        container.grid(column=0, row=0 )

        container.grid_rowconfigure(0, weight=1)

        container.grid_columnconfigure(0, weight=1)

        menu = MainPageMenu(self)
        self.config(menu=menu)

        self.frames = {}

        for F in {MainPage}:

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky='nsew')

        def show_frame(self, cont):
            frame = self.frames[cont]
            frame.tkraise()





class MainPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent) # parent is MainApp



class MainPageMenu(tk.Menu, ttk.Treeview):



    def __init__(self, parent):

        tk.Menu.__init__(self, parent)

        #Add menu
        filemenu = tk.Menu(self)
        topmenu = tk.Menu(filemenu, tearoff=0)
        self.add_cascade(label='Expense', menu=filemenu)
        filemenu.add_cascade(label='Add Expense', command=self.add_window)
        filemenu.add_cascade(label='Delete Expense', command=self.delete_window)
        filemenu.add_separator()
        self.add_cascade(label='Table')
        self.add_cascade(label='Exit', command = quit)

        cur.execute('SELECT id, Date, Name, Transaction, Category, Description, Total FROM expensetable') #grabs the data and puts it in the tree

        rows = cur.fetchall()

        self.smalldata = {}




        cur.execute('SELECT Category, Transaction FROM expensetable') #Grabs the data and puts it in the pie chart without the id interfering
        data = cur.fetchall()


        for x,y in data:
                y = int(y)
                self.smalldata[x] = self.smalldata.get(x, 0 ) + y

        for k,v in self.smalldata.items():
            k = self.smalldata.keys()
            v = self.smalldata.values()



        self.figure2 = Figure(figsize=(4.2,4), dpi=100)
        self.subplot2 = self.figure2.add_subplot(111)

        self.subplot2.pie(v, labels=k)

        pie2 = FigureCanvasTkAgg(self.figure2, self.master)
        pie2.get_tk_widget().grid(column=0, row=4)





        # Create Listing
        self.my_tree = ttk.Treeview()

        self.my_tree['columns'] = ('id','Date', 'Name', 'Transaction', 'Category', 'Description', 'Total')

        self.my_tree.column('#0', width=0, stretch=20)
        self.my_tree.column('id', width=20)
        self.my_tree.column('Date', width=120)
        self.my_tree.column('Name', width=120)
        self.my_tree.column('Transaction', width=120)
        self.my_tree.column('Category', width=120)
        self.my_tree.column('Description', width=120)
        self.my_tree.column('Total', width=120)

        self.my_tree.heading("#0")
        self.my_tree.heading('id', text='id')
        self.my_tree.heading('Date', text='Date')
        self.my_tree.heading('Name', text='Name')
        self.my_tree.heading('Transaction', text='Transaction')
        self.my_tree.heading('Category', text='Category')
        self.my_tree.heading('Description', text='Description')
        self.my_tree.heading('Total', text='Total')

        self.my_tree.grid(column=0, row=0)

        for row in rows:

            self.my_tree.insert('', tk.END ,values=row)


        try:
            cur.execute('SELECT total FROM expensetable')

            profit = cur.fetchone()

            self.Total = int(''.join(map(str, profit)))

        except:
            self.Total = 0





    def add_window(self):

        #Create New Window
        Frame = Toplevel()


        Frame.title('Another Window')

        Date_label = Label(Frame, text='Date:')
        Name_label = Label(Frame, text='Name:')
        Transaction_Label = Label(Frame, text='Transaction:')

        Description_Label = Label(Frame, text='Description:')

        Date_label.grid(column=0, row=0)
        Name_label.grid(column=0, row=1)
        Transaction_Label.grid(column=0, row=2)

        Description_Label.grid(column=0, row=3)

        self.Date_Entry = Entry(Frame)
        self.Name_Entry = Entry(Frame)
        self.Transaction_Entry = Entry(Frame)

        self.Description_Entry = Entry(Frame)

        self.Date_Entry.grid(column=1, row=0)
        self.Name_Entry.grid(column=1, row=1)
        self.Transaction_Entry.grid(column=1, row=2)

        self.Description_Entry.grid(column=1, row=3)

        Submit = Button(Frame, text='Submit', command=self.submit)
        Submit.grid(column=1, row=5, pady=20)

        self.r = tk.IntVar()

        RadioLayer = LabelFrame(Frame)
        RadioLayer.grid(column=0, row=6)

        Operation = [('Income', 1), ('Expense', -1)]

        for text, mode in Operation: #Income or Expense color coding (Not yet included), also a way to prevent accident listing of whats income and expense
            Radiobutton(RadioLayer, text=text, variable=self.r, value=mode).pack()

        self.Category = tk.StringVar()



        dropmenu = OptionMenu(Frame, self.Category, 'Income', 'Food', 'Utility', 'Subscriptions') #Allows to select which type of expense
        dropmenu.grid(column=1, row=6)

        Frame.geometry('250x250')


    def delete_window(self):
        Frame = Toplevel()

        self.delete_label = Label(Frame, text='Delete ID: ')
        self.delete_label.pack()

        self.delete_entry = Entry(Frame)
        self.delete_entry.pack()

        self.delete_button = Button(Frame, text='Delete', command = self.deletion)
        self.delete_button.pack()

        self.delete_entry.delete(0, END)



    def deletion(self):

        cur.execute('DELETE FROM expensetable WHERE id= ' + self.delete_entry.get())

        conn.commit()

        cur.execute('SELECT * FROM test')

        rows = cur.fetchall()

        for record in self.my_tree.get_children(): #Possibly need to find a better way to update a treeview after deletion
            self.my_tree.delete(record)

        for row in rows:

            self.my_tree.insert('', tk.END, values=row)

        for k,v in self.smalldata.items(): #Seperates the items to be used in the pie chart
            k = self.smalldata.keys()
            v = self.smalldata.values()

        #Why do these lines not work?
        self.figure2 = Figure(figsize=(4.2,4), dpi=100)

        self.subplot2 = self.figure2.add_subplot(111)

        self.subplot2.pie(v, labels=k)


        self.pie2 = FigureCanvasTkAgg(self.figure2, self.master) #Answer: set the 2nd one to self.master

        self.pie2.get_tk_widget().grid(column=0, row=4)



    def submit(self):
        #global count #Allows treeview to not clash with iids when submitting



        if self.r.get() == 1 and self.Category.get() == 'Income':

            try:
                self.smalldata.update(Income = smalldata['Income'] + int(self.Transaction_Entry.get()))
                print(smalldata)
            except:
                self.smalldata['Income'] = (int(self.Transaction_Entry.get()))

            self.Total+=(int(self.Transaction_Entry.get()))

            self.my_tree.set([], 'Total', self.Total) #If you ever needed to make a total column for each entry. Don't Forget this



            cur.execute("INSERT INTO expensetable (Date, Name, Transaction, Category, Description, Total) VALUES (%s, %s, %s, %s, %s, %s)", (self.Date_Entry.get(), self.Name_Entry.get(), self.Transaction_Entry.get(), self.Category.get(), self.Description_Entry.get(), self.Total))

            cur.execute("SELECT id FROM expensetable ORDER BY ID DESC")

            idnumber = cur.fetchone()

            count = int(''.join(map(str, idnumber)))


            self.my_tree.insert(parent='', index='end', iid=count, text='Parent', values=(count, self.Date_Entry.get(), self.Name_Entry.get(), self.Transaction_Entry.get(), self.Category.get(), self.Description_Entry.get(), self.Total))



            #count += 1 #Move to the next line

            #Clear the boxes
            self.Date_Entry.delete(0, END)
            self.Name_Entry.delete(0, END)
            self.Transaction_Entry.delete(0, END)

            self.Description_Entry.delete(0, END)







        elif self.r.get() == -1 and self.Category.get() != 'Income':

            self.Total+=(int(self.Transaction_Entry.get()) * -1)

            self.my_tree.set([], 'Total', self.Total) #If you ever needed to make a total column for each entry. Don't Forget this


            cur.execute("INSERT INTO expensetable (Date, Name, Transaction, Category, Description, Total) VALUES (%s, %s, %s, %s, %s, %s)", (self.Date_Entry.get(), self.Name_Entry.get(), self.Transaction_Entry.get(), self.Category.get(), self.Description_Entry.get(), self.Total))

            cur.execute("SELECT id FROM expensetable ORDER BY ID DESC ")

            idnumber = cur.fetchone()

            count = int(''.join(map(str, idnumber)))

            self.my_tree.insert(parent='', index='end', iid=count, text='Parent', values=(count, self.Date_Entry.get(), self.Name_Entry.get(), self.Transaction_Entry.get(), self.Category.get(), self.Description_Entry.get(), self.Total))

            if self.Category.get() == 'Food':

                try:
                    self.smalldata.update(Food = self.smalldata['Food'] + int(self.Transaction_Entry.get()))
                    print(self.smalldata)
                except:
                    self.smalldata['Food'] = (int(self.Transaction_Entry.get()))


            if self.Category.get() == 'Utility':

                try:
                    self.smalldata.update(Utility = self.smalldata['Utility'] + int(self.Transaction_Entry.get()))
                    print(self.smalldata)
                except:
                    self.smalldata['Utility'] = (int(self.Transaction_Entry.get()))


            if self.Category.get() == 'Subscriptions':

                try:
                    self.smalldata.update(Subscriptions = self.smalldata['Subscriptions'] + int(self.Transaction_Entry.get()))
                    print(self.smalldata)
                except:
                    self.smalldata['Subscriptions'] = (int(self.Transaction_Entry.get()))

            #count += 1 # Move to the next line

            #Clear the boxes
            self.Date_Entry.delete(0, END)
            self.Name_Entry.delete(0, END)
            self.Transaction_Entry.delete(0, END)

            self.Description_Entry.delete(0, END)

        else:
            print('Clashing Methods of Transactions')
            print(self.smalldata)


        for k,v in self.smalldata.items(): #Seperates the items to be used in the pie chart
            k = self.smalldata.keys()
            v = self.smalldata.values()

        #Why do these lines not work?
        self.figure2 = Figure(figsize=(4.2,4), dpi=100)

        self.subplot2 = self.figure2.add_subplot(111)

        self.subplot2.pie(v, labels=k)


        self.pie2 = FigureCanvasTkAgg(self.figure2, self.master) #Answer: set the 2nd one to self.master

        self.pie2.get_tk_widget().grid(column=0, row=4)


        conn.commit()







app = MainApp()
#app.geometry('400x400')
app.mainloop()
