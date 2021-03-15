# File: Custom.py
# Author: Devin DeJongh 
# Description: 
#       - Custom backtracking implementation for sudoku
#       - Intend on adding an interactive GUI in the future 

# The Algorithm:
#   1. Create a function that checks after assigning
#   a number to the current spot whether or not the grid becomes safe
#   Keep a hashmap for row column and indexes. If any number has a frequency
#   greater than one than return false otherwise true. 
#   2. Create a recursive function that takes a grid 
#   3. Check for next unassigned location. Then assign a number 1-9 
#   checking if the grid is still safe or not. If safe then recursively
#   call the function for all safe cases from 0 to 9. If any recursive call
#   returns true then end the loop and return true. 
#   4. If no more unassigned locations return True. 

board = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

def print_board(board): 
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print("\n") 

# Check if new number assignment makes board unsafe 
# board is the puzzle
# location is our current location tracker 
def next_empty(board, location):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                location[0] = i
                location[1] = j 
                return True
    return False

# Check if the number is already in the row
# board is the current puzzle state
# row is the current row
# num is the guess 
def num_in_row(board, row, num):
    for i in range(9):
        if board[row][i] == num:
            return True
    return False

# Check if the number is already in the col
# board is the current puzzle state
# col is the current col
# num is the guess
def num_in_col(board, col, num):
    for i in range(9):
        if board[i][col] == num:
            return True 
    return False

# Check the 3x3 subgrid containing the number
def num_in_sub(board, row, col, num):
    for i in range(3):
        for j in range(3):
            if(board[i + row][j + row] == num): 
                return True 
    return False 


# Check the locations safety 
def location_safe(board, row, col, num):
    return (
        not num_in_row(board, row, num) and
        not num_in_col(board, col, num) and 
        not num_in_sub(board, row - row % 3, col - col % 3, num)
    )

def solver(board):
    location = [0, 0]

    if(not next_empty(board, location)):
        return True 

    row = location[0]
    col = location[1] 

    for num in range(1,10):
        if(location_safe(board, row, col, num)):
            board[row][col] = num
            if(solver(board)):
                return True
            board[row][col] = 0
    return False 

if __name__=='__main__':
    if(solver(board)):
        print_board(board)
    else:
        print("No solution")