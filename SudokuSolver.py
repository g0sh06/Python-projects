import random

rows = 9
cols = 9
sudoku = [[0 for x in range(cols)] for y in range(rows)]


def already_exists(x, y, current_number):
    # check if current number exists in row
    if current_number in sudoku[y]:
        return True

    # check if number exist in column
    for row in sudoku:
        if row[x] == current_number:
            return True

    return False


def check_3x3_grid(x_start, y_start, current_number):
    for row in range(x_start, x_start + 3):
        for col in range(y_start, y_start + 3):
            if sudoku[row][col] == current_number:
                return True
    return False


def creating_sudoku():
    for y in range(9):
        for x in range(9):
            percentage = random.randint(1, 5)
            current_number = random.randint(1, 9)
            # finding the starting row of a 3x3 grid depending in the cell
            # for example cell (1, 2) is in the first 3x3 grid
            # Explanation y = 1, y % 3 = 1 => 1-1 = 0 and it is moving us
            # to the first element of the grid
            if percentage == 1 and 2:
                while already_exists(x, y, current_number) and check_3x3_grid(y - y % 3, x - x % 3, current_number):
                    current_number = random.randint(1, 9)
                sudoku[y][x] = current_number

def solve_the_sudoku(grid, r = 0, c = 0):
    if r == 9:
        return True
    elif c == 9:
        return solve_the_sudoku(grid, r+1, 0)
    elif grid[r][c] != 0:
        return solve_the_sudoku(grid, r, c+1)
    else:
        for y in range(1, 10):
            if not already_exists(c, r, y):
                grid[r][c] = y
                if solve_the_sudoku(grid, r, c+1):
                    return True
                grid[r][c] = 0
        return False

def printing_sudoku(sudoku):
    for y in range(rows):
        if y % 3 == 0:
            print("- " * 11)
        for x in range(cols):
            if x % 3 == 0:
                print("|", end=" ")
            print(sudoku[y][x], end=" ")
        print()


creating_sudoku()
solve_the_sudoku(sudoku)
printing_sudoku(sudoku)
