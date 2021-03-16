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

def is_valid(row, col, num, board): 
    # check row 
    for i in range(9):
        if board[row][i] == num:
            return False
    
    # check col
    for j in range(9):
        if board[j][col] == num:
            return False 

    # check block 
    block_row = row - row % 3
    block_col = col - col  % 3

    search_row = block_row
    while search_row <= block_row + 2:
        search_col = block_col 
        while search_col <= block_col + 2:
            if board[search_row][search_col] == num:
                return False 
            search_col += 1
        search_row += 1

    return True 

def solve_helper(row, col, board): 
    if row == 8 and col == 8:
        if board[row][col] != 0:
            print_board(board) 
        else:  
            for x in range(1, 10):
                if is_valid(row, col, x, board):
                    board[row][col] = x
        return
    if col > 8: 
        solve_helper(row+1, 0, board)
        return 
    if board[row][col] == 0:
        for x in range(1,10):
            if is_valid(row, col, x, board): 
                board[row][col] = x
                solve_helper(row, col+1, board)
                board[row][col] = 0
    else:
        solve_helper(row, col+1, board)
    





if __name__ == '__main__':
    print("test")