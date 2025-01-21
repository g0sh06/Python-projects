import time
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

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._create_cells()

    def _create_cells(self):
        for i in range(self._num_cols):  # Loop through columns
            col_cells = []
            for j in range(self._num_rows):  # Loop through rows
                x1 = self._x1 + i * self._cell_size_x
                y1 = self._y1 + j * self._cell_size_y
                x2 = x1 + self._cell_size_x
                y2 = y1 + self._cell_size_y
                col_cells.append(Cell(x1, x2, y1, y2, self._win.canvas))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)


class Cell:
    def __init__(self, x1,
                       x2,
                       y1,
                       y2,
                       win
                       ):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True,
        self.has_bottom_wall = True
        self.win = win
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def draw(self):
        if self.has_left_wall:
            self.win.create_line(self.x1, self.y1, self.x1, self.y2, fill="black", width = 2)
        if self.has_right_wall:
            self.win.create_line(self.x2, self.y1, self.x2, self.y2, fill="black", width = 2)
        if self.has_bottom_wall:
            self.win.create_line(self.x1, self.y2, self.x2, self.y2, fill="black", width = 2)    
        if self.has_top_wall:
            self.win.create_line(self.x1, self.y1, self.x2, self.y1, fill="black", width = 2)

    def draw_move(self, to_cell, undo=False):
        x1 = (self.x1 + self.x2) / 2
        y1 = (self.y1 + self.y2) / 2
        x2 = (to_cell.x1 + to_cell.x2) / 2
        y2 = (to_cell.y1 + to_cell.y2) / 2
        if undo == False:
            self.win.create_line(x1, y1, x2, y2, fill="red", width = 2)
        else:
            self.win.create_line(x1, y1, x2, y2, fill="gray", width = 2) 

if __name__ == "__main__":
    app = Window(800,600)
    #example line, which is working
    #point1 = Point(150,150)
    #point2 = Point(200,200)
    #point3 = Point(400,400)
    #point4 = Point(600,600)
    #cell1 = Cell(x1=point1.x, y1=point1.y, x2=point2.x, y2=point2.y, win=app.canvas)
    #cell2 = Cell(x1=point3.x, y1=point3.y, x2=point4.x, y2=point4.y, win=app.canvas)
    #cell1.draw()
    #cell2.draw()
    #cell1.draw_move(to_cell=cell2)
    maze = Maze(50, 50, 12, 16, 45, 40, app)
    app.wait_for_close()            
        