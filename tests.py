import unittest
from main import Maze, Window

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 10
        num_rows = 10
        app = Window(800,600)
        m1 = Maze(50, 50, num_rows, num_cols, 20, 20, app)
        self.assertEqual(
            len(m1._cells),
            num_cols
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

if __name__ == "__main__":
    unittest.main()
