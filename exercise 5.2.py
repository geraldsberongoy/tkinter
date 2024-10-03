from tkinter import *
from tkinter import filedialog

def open_file():
    """Open a file and display its contents in the text area."""
    filename = filedialog.askopenfilename()
    with open(filename, 'r') as file:   # Open the file
        content = file.read()           # Read the contents of the file
        text_area.delete(1.0, END)      # Clear the text area
        text_area.insert(1.0, content)  # Insert the contents of the file into the text area

def save_file():
    """Save the contents of the text area to a file."""
    filename = filedialog.asksaveasfilename(defaultextension=".txt", 
                                            filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    with open(filename, 'w') as file:       # Open the file
        content = text_area.get(1.0, END)   # Get the contents of the text area
        file.write(content)                 # Write the contents to the file
        
def convert_to_uppercase():
    """Convert the text in the text area to uppercase."""
    content = text_area.get(1.0, END)      # Get the contents of the text area
    text_area.delete(1.0, END)             # Clear the text area
    text_area.insert(1.0, content.upper()) # Insert the uppercase text into the text area

def quit_app():
    """Destroy the main window."""
    main.destroy()

# Create the main window
main = Tk()
main.title("Exercise 5.2")

text_area = Text(main, wrap=WORD, font=("Arial", 12), bg="lightgray")
text_area.pack(expand=True, fill=BOTH)

# Create a menu bar
menubar = Menu(main)

# Create a File menu
menu_file = Menu(menubar, tearoff=0)
menu_file.add_command(label="Open", command=open_file)
menu_file.add_command(label="Save", command=save_file)
menu_file.add_command(label="Quit", command=quit_app)

# Create an Edit menu
menu_edit = Menu(menubar, tearoff=0)
menu_edit.add_command(label="Convert to Uppercase", command=convert_to_uppercase)

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

# Loop to start the application
main.mainloop()