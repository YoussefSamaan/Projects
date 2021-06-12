import numpy as np

sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


def possible_solution(sudoku, column, row, number):
    for i in range(9):
        if sudoku[i][column] == number:
            return False

    for i in range(9):
        if sudoku[row][i] == number:
            return False

    cube_column_number = (column//3)*3
    cube_row_number = (row//3)*3

    for i in range(3):
        for j in range(3):
            if sudoku[cube_row_number + i][cube_column_number + j] == number:
                return False

    return True


def finding_zeros(sudoku):
    for row in range(9):
        for column in range(9):
            if sudoku[row][column] == 0:
                return row, column
    return False


def solve_sudoku(sudoku):

    to_solve = finding_zeros(sudoku)

    if not to_solve:
        return sudoku

    else:

        row, column = to_solve

    for number in range(1, 10):
        if possible_solution(sudoku, column, row, number):
            sudoku[row][column] = number
            if solve_sudoku(sudoku):
                return sudoku
            sudoku[row][column] = 0


print(np.matrix(solve_sudoku(sudoku)))
