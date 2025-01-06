import tkinter as tk

#create the window in a class
class Window:
    def __init__(self, width, height):
        self.root = tk.Tk()
        self.root.title("My Maze soler")
        self.is_running = False
        self.canvas = tk.Canvas(self.root, width = width, height = height)
        self.canvas.pack(expand = True, fill = 'both')
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()
    
    def wait_for_close(self):
        self.is_running = True
        while(self.is_running == True):
            self.redraw()

    def close(self):
        self.is_running = False       

if __name__ == "__main__":
    app = Window(800,600)
    app.wait_for_close()            
        