from tkinter import *

# Set up the main window
main = Tk()
main.title("Exercise 3")  
main.geometry("200x200")  
main.resizable(1, 1)

# Create a frame on the left side of the window
frame_left = Frame(main)
frame_left.pack(side=LEFT, fill=BOTH, expand=True)  # Fill the left half of the window

# Create a frame on the right side of the window
frame_right = Frame(main)
frame_right.pack(side=RIGHT, fill=BOTH, expand=True)  # Fill the right half of the window

# Create a frame in the top half of the left frame
frame_left_top = Frame(frame_left, bg="blue", bd=2, relief="groove")
frame_left_top.pack(side=TOP, fill=BOTH, expand=True)  # Fill the top half of the left frame

# Create a frame in the bottom half of the left frame
frame_left_bottom = Frame(frame_left, bd=2, relief="groove")
frame_left_bottom.pack(side=BOTTOM, fill=BOTH, expand=True)  # Fill the bottom half of the left frame

# Create a frame in the top half of the right frame
frame_right_top = Frame(frame_right, bd=2, relief="groove")
frame_right_top.pack(side=TOP, fill=BOTH, expand=True)  # Fill the top half of the right frame

# Create a frame in the bottom half of the right frame
frame_right_bottom = Frame(frame_right, bg="blue", bd=2, relief="groove")
frame_right_bottom.pack(side=BOTTOM, fill=BOTH, expand=True)  # Fill the bottom half of the right frame

# Add a label to the top left frame
label_top_left = Label(frame_left_top, text="A", bg="blue")
label_top_left.place(relx=0.5, rely=0.5, anchor=CENTER)  # Center the label in the frame

# Add a label to the bottom left frame
label_bottom_left = Label(frame_left_bottom, text="B")
label_bottom_left.place(relx=0.5, rely=0.5, anchor=CENTER)  # Center the label in the frame

# Add a label to the top right frame
label_top_right = Label(frame_right_top, text="C")
label_top_right.place(relx=0.5, rely=0.5, anchor=CENTER)  # Center the label in the frame

# Add a label to the bottom right frame
label_bottom_right = Label(frame_right_bottom, text="D", bg="blue")
label_bottom_right.place(relx=0.5, rely=0.5, anchor=CENTER)  # Center the label in the frame

# Start the main event loop
main.mainloop()