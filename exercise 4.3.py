from tkinter import *
from tkinter import colorchooser, simpledialog, messagebox
import re

# Initialize global variables for shape, fill, color, and mode
current_shape = 's'  # 's' for square, 'c' for circle
current_fill = 'f'  # 'F' for filled, 'f' for unfilled
current_color = 'yellow'  # Default color
canvas_bg_color = 'gray'  # Default canvas background color
pen_mode = False  # Start in shape drawing mode

def draw_shape(event):
    """Draw the current shape on the canvas at the mouse click position."""
    if not pen_mode:
        # Size of the shape
        shape_size = 40
        # Get the mouse click position
        x = event.x
        y = event.y

        # Determine the fill option
        fill_option = current_color if current_fill == 'F' else ""

        if current_shape == 's':
            # Draw a square
            canvas.create_rectangle(x, y, x + shape_size, y + shape_size, outline=current_color, fill=fill_option)
        elif current_shape == 'c':
            # Draw a circle
            canvas.create_oval(x, y, x + shape_size, y + shape_size, outline=current_color, fill=fill_option)

        # Update the status label with the coordinates and current options
        shape = 'Square' if current_shape == 's' else 'Circle'
        status_label.config(text=f"Status: {shape} at ({x}, {y}) in {current_color}, filled: {current_fill == 'F'}")

def start_pen_mode(event):
    """Start drawing in pen mode."""
    global pen_mode, last_x, last_y
    pen_mode = True
    last_x, last_y = event.x, event.y

def draw_pen(event):
    """Draw in pen mode by creating a line to the current mouse position."""
    global last_x, last_y
    if pen_mode:
        canvas.create_line(last_x, last_y, event.x, event.y, fill=current_color)
        last_x, last_y = event.x, event.y

def stop_pen_mode(event):
    """Stop drawing in pen mode."""
    global pen_mode
    pen_mode = False

def set_shape_square():
    """Set the shape to square."""
    global current_shape
    current_shape = 's'
    status_label.config(text="Status: Shape set to Square")

def set_shape_circle():
    """Set the shape to circle."""
    global current_shape
    current_shape = 'c'
    status_label.config(text="Status: Shape set to Circle")

def set_fill_filled():
    """Set the fill option to filled."""
    global current_fill
    current_fill = 'F'
    status_label.config(text="Status: Fill set to Filled")

def set_fill_unfilled():
    """Set the fill option to unfilled."""
    global current_fill
    current_fill = 'f'
    status_label.config(text="Status: Fill set to Unfilled")

def set_color_from_palette():
    """Open color chooser dialog and set the color."""
    global current_color
    color_code = colorchooser.askcolor(title="Choose color")[1]  # Returns (color, hex) tuple; get hex value
    if color_code:
        current_color = color_code
        status_label.config(text=f"Status: Color set to {current_color}")

def set_color_from_hex():
    """Open dialog to input hex color and set the color."""
    global current_color
    color_code = simpledialog.askstring("Input Hex Color", "Enter Hex Color (e.g. #RRGGBB):")
    if color_code:
        # Validate the hex color code format
        if not re.match(r'^#[0-9a-fA-F]{6}$', color_code):
            messagebox.showerror("Error", "Invalid Hex Color format. Please enter a valid hex color (e.g., #RRGGBB).")
            return
        
        current_color = color_code
        status_label.config(text=f"Status: Color set to {current_color}")

def set_canvas_bg_color():
    """Set the background color of the canvas."""
    global canvas_bg_color
    color_code = colorchooser.askcolor(title="Choose background color")[1]  # Returns (color, hex) tuple; get hex value
    if color_code:
        canvas_bg_color = color_code
        canvas.config(bg=canvas_bg_color)
        status_label.config(text=f"Status: Canvas background color set to {canvas_bg_color}")

def set_canvas_bg_color_from_hex():
    """Open dialog to input hex color and set the canvas background color."""
    global canvas_bg_color
    color_code = simpledialog.askstring("Input Hex Color", "Enter Hex Color (e.g. #RRGGBB):")
    if color_code:
        # Validate the hex color code format
        if not re.match(r'^#[0-9a-fA-F]{6}$', color_code):
            messagebox.showerror("Error", "Invalid Hex Color format. Please enter a valid hex color (e.g., #RRGGBB).")
            return
        
        canvas_bg_color = color_code
        canvas.config(bg=canvas_bg_color)
        status_label.config(text=f"Status: Canvas background color set to {canvas_bg_color}")

def show_instructions():
    """Show instructions on how to use the program."""
    messagebox.showinfo("Instructions", 
        "To draw shapes:\n"
        "- Left-click to draw the current shape (Square or Circle).\n"
        "- Right-click and drag to draw freehand lines.\n\n"
        "Use the Shape, Fill, and Color menus to change drawing options.")

def show_about():
    """Show information about the program."""
    messagebox.showinfo("About", 
        "Exercise 4.3: Interface Design\n"
        "This program allows you to draw squares, circles, and more shapes.\n"
        "Created by Gerald S. Berongoy, June 2024.")

def on_resize(event):
    """Handle the canvas resizing."""
    canvas.config(width=event.width, height=event.height)

# Create the main window
main = Tk()
main.title("Exercise 4.3")
main.geometry("800x623")

# Create a canvas widget
canvas = Canvas(main, bg=canvas_bg_color)
canvas.pack(fill=BOTH, expand=True)

# Bind the left mouse click event to the draw_shape function
canvas.bind("<Button-1>", draw_shape)
# Bind mouse events for pen mode
canvas.bind("<ButtonPress-3>", start_pen_mode)  # Right mouse button press to start pen mode
canvas.bind("<B3-Motion>", draw_pen)  # Right mouse button motion to draw in pen mode
canvas.bind("<ButtonRelease-3>", stop_pen_mode)  # Right mouse button release to stop pen mode

# Bind the <Configure> event to handle resizing
main.bind("<Configure>", on_resize)

# Create a status label
status_label = Label(canvas, text="Status: Ready", bd=1, relief=SUNKEN, anchor=W)
status_label.pack(side=BOTTOM, fill=X)

# Create a menu bar
menubar = Menu(main)

# Shape menu
shape_menu = Menu(menubar, tearoff=0)
shape_menu.add_command(label="Square", command=set_shape_square)
shape_menu.add_command(label="Circle", command=set_shape_circle)
menubar.add_cascade(label="Shape", menu=shape_menu)

# Fill menu
fill_menu = Menu(menubar, tearoff=0)
fill_menu.add_command(label="Filled", command=set_fill_filled)
fill_menu.add_command(label="Unfilled", command=set_fill_unfilled)
menubar.add_cascade(label="Fill", menu=fill_menu)

# Color menu
color_menu = Menu(menubar, tearoff=0)
color_menu.add_command(label="Choose Color", command=set_color_from_palette)
color_menu.add_command(label="Enter Hex Color", command=set_color_from_hex)
color_menu.add_separator()
color_menu.add_command(label="Set Canvas BG Color", command=set_canvas_bg_color)
color_menu.add_command(label="Enter Canvas BG Hex Color", command=set_canvas_bg_color_from_hex)
menubar.add_cascade(label="Color", menu=color_menu)

# Help menu
help_menu = Menu(menubar, tearoff=0)
help_menu.add_command(label="Instructions", command=show_instructions)
help_menu.add_command(label="About", command=show_about)
menubar.add_cascade(label="Help", menu=help_menu)

# Configure the menu
main.config(menu=menubar)

# Start the Tkinter event loop
main.mainloop()
