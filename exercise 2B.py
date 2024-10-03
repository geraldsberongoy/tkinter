from tkinter import *

# Event handler for the button
def clicked():
    entered_text = entry1.get()
    label1.config(text=entered_text)

# Set up the main window
app = Tk()
app.title("GUI Exercise 2B")
app.geometry("260x120")

# Entry widget for user input
entry1 = Entry(app, 
               font=("Arial", 12), 
               width=20)
entry1.pack(pady=10)

# Button widget to trigger the event handler
button1 = Button(app, 
            text="Click Me", 
            command=clicked,
            font=("Arial", 12))
button1.pack()

# Label widget to display the text
label1 = Label(app, 
            text="Text is displayed here", 
            font=("Arial", 12))
label1.pack()

app.mainloop()