import tkinter as tk

# Initialize global variables for shape, fill, color, and mode
current_shape = 's'  # 's' for square, 'c' for circle
current_fill = 'f'  # 'F' for filled, 'f' for unfilled
current_color = 'yellow'  # Default color
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

def set_color_yellow():
    """Set the color to yellow."""
    global current_color
    current_color = 'yellow'
    status_label.config(text="Status: Color set to Yellow")

def set_color_red():
    """Set the color to red."""
    global current_color
    current_color = 'red'
    status_label.config(text="Status: Color set to Red")

def set_color_green():
    """Set the color to green."""
    global current_color
    current_color = 'green'
    status_label.config(text="Status: Color set to Green")

def set_color_blue():
    """Set the color to blue."""
    global current_color
    current_color = 'blue'
    status_label.config(text="Status: Color set to Blue")

def on_resize(event):
    """Handle the canvas resizing."""
    canvas.config(width=event.width, height=event.height)

# Create the main window
main = tk.Tk()
main.title("Exercise 4.2")
main.geometry("800x623")

# Create a canvas widget
canvas = tk.Canvas(main, bg="gray")
canvas.pack(fill=tk.BOTH, expand=True)

# Bind the left mouse click event to the draw_shape function
canvas.bind("<Button-1>", draw_shape)
# Bind mouse events for pen mode
canvas.bind("<ButtonPress-3>", start_pen_mode)  # Right mouse button press to start pen mode
canvas.bind("<B3-Motion>", draw_pen)  # Right mouse button motion to draw in pen mode
canvas.bind("<ButtonRelease-3>", stop_pen_mode)  # Right mouse button release to stop pen mode

# Bind the <Configure> event to handle resizing
main.bind("<Configure>", on_resize)

# Create a status label
status_label = tk.Label(main, text="Status: Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_label.pack(side=tk.BOTTOM, fill=tk.X)

# Create a menu bar
menubar = tk.Menu(main)

# Shape menu
shape_menu = tk.Menu(menubar, tearoff=0)
shape_menu.add_command(label="Square", command=set_shape_square)
shape_menu.add_command(label="Circle", command=set_shape_circle)
menubar.add_cascade(label="Shape", menu=shape_menu)

# Fill menu
fill_menu = tk.Menu(menubar, tearoff=0)
fill_menu.add_command(label="Filled", command=set_fill_filled)
fill_menu.add_command(label="Unfilled", command=set_fill_unfilled)
menubar.add_cascade(label="Fill", menu=fill_menu)

# Color menu
color_menu = tk.Menu(menubar, tearoff=0)
color_menu.add_command(label="Yellow", command=set_color_yellow)
color_menu.add_command(label="Red", command=set_color_red)
color_menu.add_command(label="Green", command=set_color_green)
color_menu.add_command(label="Blue", command=set_color_blue)
menubar.add_cascade(label="Color", menu=color_menu)

# Configure the menu
main.config(menu=menubar)

# Start the Tkinter event loop
main.mainloop()
