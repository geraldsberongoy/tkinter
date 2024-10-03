from tkinter import *
from tkinter import filedialog, messagebox

filename = None
is_saved = True

def on_key(event):
    """Key event handler to update the status when the text area is modified."""
    global is_saved
    is_saved = False
    update_status()

def update_status():
    """Update the status label based on the saved status."""
    status = "Saved" if is_saved else "Unsaved"
    status_label.config(text=f"Status: {status}")

def open_file():
    """Open a file and display its contents in the text area."""
    global filename, is_saved
    
    # Check if the user wants to open a file
    if not is_saved and text_area.get(1.0, END).strip() != "":
        # Add checks for unsaved changes and ask the user if they want to open a file
        answer = messagebox.askquestion("Open", "Do you want to open a file?\nUnsaved changes will be lost.", icon='warning')
        if answer == "no":
            return
    
    # Open the file and display its contents in the text area
    try:
        selected_filename = filedialog.askopenfilename()
        if selected_filename:
            with open(selected_filename, 'r') as file:
                content = file.read()
                text_area.delete(1.0, END)
                text_area.insert(1.0, content)
                filename = selected_filename
                is_saved = True
                update_status()
                
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while opening the file:\n{e}")

def save_file():
    """Save the contents of the text area to a file."""
    global is_saved, filename
    
    if text_area.get(1.0, END).strip() == "" :
        messagebox.showerror("Error", "The text area is empty.\nNothing to save.")
        return
    
    if is_saved:
        messagebox.showinfo("Info", "The file has already been saved.")
        return
    
    try:
        if filename:
            answer = messagebox.askquestion("Overwrite", "Do you want to overwrite the existing file?", icon='warning')
            if answer == "no":
                filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        else:
            filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        
        if filename:
            with open(filename, 'w') as file:
                content = text_area.get(1.0, END).strip()
                file.write(content)
                is_saved = True
                update_status()
                messagebox.showinfo("Success", f"The file '{filename}' has been saved successfully.")
                
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while saving the file:\n{e}")

def convert_to_uppercase():
    """Convert the text in the text area to uppercase."""
    if text_area.get(1.0, END).strip() == "":
        messagebox.showerror("Error", "The text area is empty.\nNothing to convert.")
        return
    content = text_area.get(1.0, END)
    text_area.delete(1.0, END)
    text_area.insert(1.0, content.upper())
    global is_saved
    is_saved = False
    update_status()
    
def show_help():
    """Show instructions on how to use the program."""
    messagebox.showinfo("Instructions", 
        "Text Editor Help\n\n"
        "This program allows you to create, open, and save text files, as well as convert text to uppercase.\n\n"
        "How to use the features:\n"
        "- Open a file: Go to File > Open to open an existing text file. Any unsaved changes will be lost.\n"
        "- Save a file: Go to File > Save to save your current work. If the file is new, you will be prompted to provide a file name.\n"
        "- Convert to Uppercase: Go to Edit > Convert to Uppercase to convert all text in the editor to uppercase.\n"
        "- Quit: Go to File > Quit to exit the application. If you have unsaved changes, you will be prompted to save them before quitting.\n\n"
        "Additional Information:\n"
        "- The status bar at the bottom of the window indicates whether your changes are saved or unsaved.\n"
        "- You can find more information about this program in the About menu.\n\n"
        "If you encounter any issues, please check the About menu for the author's contact information.")


def show_about():
    """Show information about the program."""
    messagebox.showinfo("About", 
        "Text Editor Application\n"
        "Version: 1.0\n"
        "This program is a simple text editor that allows users to type, open text files, "
        "save their work, and convert text to uppercase.\n\n"
        "Features:\n"
        "- Type and edit text\n"
        "- Open and save text files\n"
        "- Convert text to uppercase\n"
        "- View help instructions\n"
        "- Status indicator for saved/unsaved changes\n\n"
        "Created by Gerald S. Berongoy, June 2024.")

def quit_app():
    """Destroy the main window."""
    if not is_saved:
        answer = messagebox.askquestion("Quit", "You have unsaved changes. Do you want to quit without saving?")
        if answer == "yes":
            main.destroy()
    else:
        main.destroy()

# Create the main window
main = Tk()
main.title("Exercise 5.3")

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
menu_about.add_command(label="Help", command=show_help)
menu_about.add_command(label="About", command=show_about)

# Add the menus to the menu bar
menubar.add_cascade(label="File", menu=menu_file)
menubar.add_cascade(label="Edit", menu=menu_edit)
menubar.add_cascade(label="Help", menu=menu_about)

# Create the text area
text_area = Text(main, wrap=WORD, font=("Arial", 12), bg="lightgray")
text_area.pack(expand=True, fill=BOTH)
text_area.bind("<Key>", on_key)

# Create the status label
status_label = Label(main, text="Status: Saved", bd=1, relief=SUNKEN, anchor=W)
status_label.pack(side=BOTTOM, fill=X)

# Add the menu bar to the main window
main.config(menu=menubar)

# Loop to start the application
main.mainloop()
