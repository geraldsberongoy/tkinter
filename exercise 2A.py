# Import everything from the tkinter module
from tkinter import *

# Event handler for the button
def clicked():
    """Change the text of the label widget when the button is clicked."""
    current_text = label1.cget("text")
    if current_text == "Displayed Text":
        label1.config(text="Alternate Text")
    else:
        label1.config(text="Displayed Text")

# Create the main window
app = Tk()
app.title("GUI Exercise 2A")
app.geometry("300x300")

# Create a new button widget
button1 = Button(app, 
            text="Click Me", 
            command=clicked, 
            font=("Arial", 12))  

# Create a new label widget
label1 = Label(app, 
            text="Displayed Text",  
            font=("Arial", 12))

# Place the widgets in the window
button1.place(relx=0.5, rely=0.45, anchor=CENTER)
label1.place(relx=0.5, rely=0.55, anchor=CENTER)

# Start the tkinter event loop
app.mainloop()