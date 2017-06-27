"""
A program that stores this book information
Title, Author, Year, ISBN

User can:   - View all records
            - Search an entry
            - Add entry
            - Update entry
            - Delete
            - Close
"""
from tkinter import *
from app_backend import Database

# Create instance of database class
database = Database()

# Define the commands
def clear_text_boxes():
    # Clear the entry boxes
    title_entry.delete(0, END)
    author_entry.delete(0, END)
    year_entry.delete(0, END)
    isbn_entry.delete(0, END)

def get_selected_row(event):
    global selected_tuple
    index = list_one.curselection()[0]
    selected_tuple = list_one.get(index)

    # Clear text boxes
    clear_text_boxes()

    # add selected values to the box
    title_entry.insert(END,selected_tuple[1])
    author_entry.insert(END,selected_tuple[2])
    year_entry.insert(END,selected_tuple[3])
    isbn_entry.insert(END,selected_tuple[4])

def view_command():
    clear_text_boxes()
    list_one.delete(0,END)
    for row in database.view():
        list_one.insert(END,row)

def search_command():
    list_one.delete(0,END)
    for row in database.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list_one.insert(END,row)

def insert_command():
    database.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list_one.delete(0,END)
    list_one.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))
    view_command()

def delete_command():
    database.delete(selected_tuple[0])
    view_command()

def update_command():
    database.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    view_command()
def close_command():
    main_window.destroy()


main_window = Tk()
main_window.title("BookStore")

# Ceate labels
l1 = Label(main_window,text="Title")
l1.grid(row=0,column=0)
l2 = Label(main_window,text="Author")
l2.grid(row=0,column=2)
l3 = Label(main_window,text="Year")
l3.grid(row=1,column=0)
l4 = Label(main_window,text="ISBN")
l4.grid(row=1,column=2)

# Create entries
title_text= StringVar()
title_entry = Entry(main_window,textvariable=title_text)
title_entry.grid(row=0,column=1)

author_text= StringVar()
author_entry = Entry(main_window,textvariable=author_text)
author_entry.grid(row=0,column=3)

year_text= StringVar()
year_entry = Entry(main_window,textvariable=year_text)
year_entry.grid(row=1, column=1)

isbn_text= StringVar()
isbn_entry = Entry(main_window,textvariable=isbn_text)
isbn_entry.grid(row=1,column=3)

# Create the listbox
list_one = Listbox(main_window, height=6,width=35)
list_one.grid(row=2,column=0,rowspan=6,columnspan=2)

# Create scrollbar
scrollbar = Scrollbar(main_window)
scrollbar.grid(row=2,column=2, rowspan=6)

# Add the scrollbar to the list
list_one.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=list_one.yview())

# Bind method on the list
list_one.bind('<<ListboxSelect>>',get_selected_row)

# Create the buttons
view_button = Button(main_window,text="View all", width=12, command=view_command)
view_button.grid(row=2,column=3)
search_button=Button(main_window,text="Search entry", width=12, command=search_command)
search_button.grid(row=3,column=3)
add_button = Button(main_window,text="Add entry", width=12, command=insert_command)
add_button.grid(row=4,column=3)
update_button = Button(main_window,text="Update Selected", width=12, command=update_command)
update_button.grid(row=5,column=3)
delete_button = Button(main_window,text='Delete Selected', width=12, command=delete_command)
delete_button.grid(row=6,column=3)
close_button = Button(main_window,text="Close", width=12, command=close_command)
close_button.grid(row=7,column=3)

main_window.mainloop()
