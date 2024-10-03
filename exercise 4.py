import tkinter as tk

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Exercise 4")
        
        self.canvas = tk.Canvas(self.root, bg="blue", width=500, height=400)
        self.canvas.pack()
        
        self.current_shape = "square"
        self.current_fill = "unfilled"
        self.current_color = "yellow"
        
        self.canvas.bind("<Button-1>", self.draw_shape)
        self.root.bind("<Key>", self.change_options)

    def draw_shape(self, event):    
        size = 50
        x, y = event.x, event.y
        
        if self.current_shape == "square":
            if self.current_fill == "filled":
                self.canvas.create_rectangle(x, y, x + size, y + size, fill=self.current_color)
            else:
                self.canvas.create_rectangle(x, y, x + size, y + size, outline=self.current_color)
        elif self.current_shape == "circle":
            if self.current_fill == "filled":
                self.canvas.create_oval(x, y, x + size, y + size, fill=self.current_color)
            else:
                self.canvas.create_oval(x, y, x + size, y + size, outline=self.current_color)

    def change_options(self, event):
        key = event.char
        if key == 's':
            self.current_shape = "square"
        elif key == 'c':
            self.current_shape = "circle"
        elif key == 'F':
            self.current_fill = "filled"
        elif key == 'f':
            self.current_fill = "unfilled"
        elif key == 'y':
            self.current_color = "yellow"
        elif key == 'r':
            self.current_color = "red"
        elif key == 'g':
            self.current_color = "green"
        elif key == 'b':
            self.current_color = "blue"
        
        print(f"Shape: {self.current_shape}, Fill: {self.current_fill}, Color: {self.current_color}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()
