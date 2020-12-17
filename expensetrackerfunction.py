import expensetrackergui
import expensetrackerguifunction

count = 0

def submit():

    my_tree.insert(parent='', index='end', iid=count, text='Parent', values=(Date_Entry.get(), Name_Entry.get(), Transaction_Label.get(), Category_Label.get(), Description_Label.get()))
    count += 1
    #Clear the boxes
    Date_label.delete(0, END)
    Name_label.delete(0, END)
    Transaction_Label.delete(0, END)
    Category_Label.delete(0, END)
    Description_Label.delete(0, END)
