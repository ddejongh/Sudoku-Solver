board = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
          [5, 2, 0, 0, 0, 0, 0, 0, 0],
          [0, 8, 7, 0, 0, 0, 0, 3, 1],
          [0, 0, 3, 0, 1, 0, 0, 8, 0],
          [9, 0, 0, 8, 6, 3, 0, 0, 5],
          [0, 5, 0, 0, 9, 0, 6, 0, 0],
          [1, 3, 0, 0, 0, 0, 2, 5, 0],
          [0, 0, 0, 0, 0, 0, 0, 7, 4],
          [0, 0, 5, 2, 0, 6, 3, 0, 0]]  

# Basic utility function, print the board
def print_board(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print("\n")

def next_empty_location(board, location):
    for i in range(9):
        for j in range(9):
            if(board[i][j]==0):
                location[0] = i
                location[1] = j 
                return True
    return False 

def check_row(board, row, num):
    for i in range(9):
        if(board[row][i] == num):
            return True
    return False 

def check_col(board, col, num):
    for i in range(9):
        if(board[i][col] == num): 
            return True
    return False 

def check_subgrid(board, row, col, num):
    for i in range(3):
        for j in range(3):
            if(board[i + row][j + col] == num):
                return True
    return False 

def check_location(board, row, col, num):
    return (not check_row(board, row, num)) and (not check_col(board, row, num)) and (not check_subgrid(board, row - row % 3, col - col % 3, num))

def solve(board): 
    location = [0, 0]

    if(not next_empty_location(board, location)):
        return True

    row = location[0]
    col = location[1]

    for num in range(1, 10):
        if(check_location(board, row, col, num)) :
            board[row][col] = num 
            if(solve(board)):
                return True
            board[row][col] = 0
    return False

if __name__=="__main__":
    # print_board(board)

    if(solve(board)):
        print_board(board)
    else:
        print("Impossible board")