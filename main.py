import tkinter as tk

#create the window in a class
class Window:
    def __init__(self, width, height):
        self.root = tk.Tk()
        self.root.title("My Maze soler")
        self.is_running = False
        self.canvas = tk.Canvas(self.root, width = width, height = height)
        self.canvas.pack(expand = True, fill = 'both')

    def run(self):
        self.is_running = True
        self.root.mainloop()

if __name__ == "__main__":
    app = Window(800,600)
    app.run()            
        