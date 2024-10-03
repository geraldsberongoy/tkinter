from tkinter import *

def draw_square(event):
    """Draw a square on the canvas at the mouse click position and update the status label."""
    
    # Size of the square
    square_size = 40
    # Get the mouse click position
    x = event.x
    y = event.y
    # Draw the square
    canvas.create_rectangle(x, y, x + square_size, y + square_size, outline="black", fill="blue")
    # Update the status label with the coordinates
    status_label.config(text=f"Status: Clicked at ({x}, {y})")

# Create the main window
main = Tk()
main.title("Exercise 4.1")
main.geometry("800x623")

# Create a canvas widget
canvas = Canvas(main, width=800, height=600, bg="gray")
canvas.pack()

# Bind the left mouse click event to the draw_square function
canvas.bind("<Button-1>", draw_square)

# Create a status label
status_label = Label(main, text="Status: Ready", bd=1, relief=SUNKEN, anchor=W)
status_label.pack(side=BOTTOM, fill=X)

# Start the Tkinter event loop
main.mainloop()