from tkinter import *

# Action Button_One will preform when clicked
def km_to_miles():
    text_widget.delete('1.0', END)
    miles = float(entry_widget_value.get())*1.60
    text_widget.insert(END,str(miles))
# Create the window
window = Tk()

 #create widgets(button,...) between creation of the window and window.mainloop()
 # Button widget
button_one = Button(window,text="Execute",command=km_to_miles)

# Setup a variable for the value people enter in the entry_widget
entry_widget_value = StringVar()
entry_widget = Entry(window,textvariable=entry_widget_value)

# Create a text widget
text_widget = Text(window,height=1,width=20)

# Adding the button to the window and placing it on the window grid
button_one.grid(row=0,column=0)
entry_widget.grid(row=0,column=1)
text_widget.grid(row=0,column=2)

#




window.mainloop()
