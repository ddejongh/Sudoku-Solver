# File: Solver.py
# Author: Devin DeJongh - github.com/ddejongh
# Description: 
#       - Solver for Sudoku using backtracking algorithm. 
#       - Should be nice, I have no idea what I'm doing.
#       - Will eventually update with a GUI version using pygame I think
import time
import sys

sys.setrecursionlimit(9000)

# lets start with a static board configuration found online 
board = [
    [0, 0, 4, 0, 0, 0, 3, 0, 0],
    [2, 0, 0, 7, 0, 9, 0, 0, 8],
    [0, 6, 0, 5, 0, 4, 0, 7, 0],
    [0, 0, 5, 0, 7, 0, 2, 0, 0],
    [4, 0, 0, 3, 0, 5, 0, 0, 9],
    [0, 0, 7, 0, 9, 0, 5, 0, 0], 
    [0, 4, 0, 9, 0, 2, 0, 5, 0],
    [8, 0, 0, 6, 0, 7, 0, 0, 2],
    [0, 0, 9, 0, 0, 0, 1, 0, 0]
]

# Utility function for printing grid 
def print_grid(puzzle): 
    for row in range(9):
        for col in range(9):
            print(puzzle[row][col], end=" "),
        print('\n')

# Find the next empty spot in the board
# l keeps track of incrementation 
def find_empty_spot(arr, l): 
    for row in range(9):
        for col in range(9):
            l[0] = row
            l[1] = col
            return True 
    return False 

# Is there a matching value in the same row?
def check_row(arr, row, num): 
    for i in range(9):
        if(arr[row][i] == num):
            return True
    return False

# Is there a matching value in the same column?
def check_col(arr, col, num):
    for i in range(9):
        if(arr[i][col] == num):
            return True
    return False

# Is there a matching number in its 3x3 grid? 
def check_subgrid(arr, row, col, num):
    for i in range(3):
        for j in range(3):
            if(arr[i+row][j+col] == num):
                return True 
    return False 

# Check the location based on the row, column, and subgrid
def check_location(arr, row, col, num):
    return not check_row(arr, row, num) and not check_col(arr, col, num) and not check_subgrid(arr, row - row % 3, col - col % 3, num)

def solve_sudoku(puzzle): 
    # keep track of location 
    l = [0, 0]

    if(not find_empty_spot(puzzle, l)):
        return True

    row = l[0]
    col = l[1]

    for num in range(1,10):
        if(check_location(puzzle, row, col, num)):
            
            puzzle[row][col] = num

            if(solve_sudoku(puzzle)):
                return True 

            puzzle[row][col] = 0

    return False

# Driver function here
if __name__ == "__main__":

    # print_grid(board)
    # print('Testing testing')

    if(solve_sudoku(board)):
        print_grid(board)
    else:
        print("Impossible puzzle")
