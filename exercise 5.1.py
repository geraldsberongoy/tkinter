from tkinter import *

# Create the main window
main = Tk()
main.title("Exercise 5.1")

# Create a menu bar
menubar = Menu(main)

# Create a File menu
menu_file = Menu(menubar, tearoff=0)
menu_file.add_command(label="Open")
menu_file.add_command(label="Save")
menu_file.add_command(label="Quit")

# Create an Edit menu
menu_edit = Menu(menubar, tearoff=0)
menu_edit.add_command(label="Convert to Uppercase")

# Create an About menu
menu_about = Menu(menubar, tearoff=0)
menu_about .add_command(label="Help") 
menu_about .add_command(label="About")

# Add the menus to the menu bar
menubar.add_cascade(label="File", menu=menu_file)
menubar.add_cascade(label="Edit", menu=menu_edit)
menubar.add_cascade(label="Help", menu=menu_about)

# Add the menu bar to the main window
main.config(menu=menubar)

main.mainloop()