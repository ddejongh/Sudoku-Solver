# File: Custom_solver.py
# Author: Devin DeJongh 
# Description: 
#       - Custom backtracking implementation for sudoku
#       - Intend on adding an interactive GUI in the future 

board = [
    [0, 0, 2, 0, 0, 5, 0, 7, 9],
    [1, 0, 5, 0, 0, 3, 0,  0, 0],
    [0, 0, 0, 0, 0, 0, 6, 0, 0],
    [0, 1, 0, 4, 0, 0, 9, 0, 0],
    [0, 9, 0, 0, 0, 0, 0, 8, 0],
    [0, 0, 4, 0, 0, 9, 0, 1, 0],
    [0, 0, 9, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 3, 0, 6],
    [6, 8, 0, 3, 0, 0, 4, 0, 0],
]

def print_board(board): 
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print("\n") 

if __name__=='__main__':
    print("Printing from main")

    print_board(board)