# File: Solver.py
# Author: Devin DeJongh - github.com/ddejongh
# Description: 
#       - Solver for Sudoku using backtracking algorithm. 
#       - Should be nice, I have no idea what I'm doing.
# 
#       - Will eventually update with a GUI version using pygame I think
import time

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

def print_grid(puzzle): 
    for row in range(9):
        for col in range(9):
            print(puzzle[row][col], end=" "),
        print('\n')

print_grid(board)
