from tkinter import *

# Event handler for the button
def clicked():
    """Event that changes the widgets when the button is clicked."""
    entered_text = entry1.get()
    
    # Change the text of the label widget and color of the button if therre is no input
    if entered_text == "":
        button1.config(bg="red",
                       text="Enter some text")
    
    else:
        # Changes the text of the label widget and color of the button if there is an input
        if button1.cget("text") == "Clear the Entry":
            entry1.delete(0, END)
            button1.config(bg="white", 
                           text="Enter some text")
            label1.config(text="Input text is displayed here")
        else:
            button1.config(bg="white", 
                           text="Clear the Entry")
            label1.config(text=entered_text)

# Set up the main window
app = Tk()
app.title("GUI Exercise 2.3")
app.geometry("260x120")

# Entry widget for user input
entry1 = Entry(app, 
               font=("Arial", 12), 
               width=20)
entry1.pack(pady=10)

# Button widget to trigger the event handler
button1 = Button(app, 
            text="Enter some text", 
            command=clicked,
            font=("Arial", 12))
button1.pack()

# Label widget to display the text
label1 = Label(app, 
            text="Input text is displayed here", 
            font=("Arial", 12))
label1.pack()

app.mainloop()