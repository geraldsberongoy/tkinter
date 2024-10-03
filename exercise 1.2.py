#Import the Tkinter  package
from tkinter import *

# # Exercise 1.1
# # This method is called when the button is pressed 
# def clicked():
#     print("Clicked")
    
# #Create a main frame  with a title and size 200 by 200 pixels
# app = Tk()
# app.title("GUI Example 1")
# app.geometry('200x200')

# #Create the button
# button1 = Button(app, text="Click Here", command=clicked) 
# button1.pack(side='bottom')

# # Start the application running
# app.mainloop()

# Exercise 1.2
def clicked():
    print("I am clicked!")
    
#Create a main frame 
app = Tk()

#Renaming the title
app.title("First GUI Example")

#Resizing to 300 by 300 pixels
app.geometry('450x300')

#Create the button
button1 = Button(app, text="Click Me Pls", command=clicked)
button1.pack(side='top', pady=20, padx=20, fill=X)

#Start the application running
app.mainloop()