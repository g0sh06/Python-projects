import tkinter as tk

#create the window in a class
class Window:
    def __init__(self, width, height):
        self.root = tk.Tk()
        self.root.title("My Maze soler")
        self.is_running = False
        self.canvas = tk.Canvas(self.root, width = width, height = height, bg="white")
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

    def draw_line(self, line, fill_color="black"):
        line.draw(self.canvas, fill_color)      

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2
        )

                   


if __name__ == "__main__":
    app = Window(800,600)
    #example line, which is working
    point1 = Point(300,300)
    point2 = Point(500, 500)
    line = Line(point1=point1, point2=point2)
    app.draw_line(line=line)

    app.wait_for_close()            
        