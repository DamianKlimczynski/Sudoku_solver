import time

def solve_sudoku(board):
     
		# Solves a Sudoku puzzle using backtracking.
    
    empty_cell = find_empty_cell(board)
    
    if not empty_cell:
        return True
    else:
        row, col = empty_cell

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False

def is_valid(board, num, pos):
    
    # Checks if it's valid to place 'num' at 'pos' in the Sudoku board.
 
    row, col = pos
    
    # Check row
    if num in board[row]:
        return False

    # Check column
    if num in [board[i][col] for i in range(9)]:
        return False

    # Check box
    box_start_row, box_start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(box_start_row, box_start_row + 3):
        for j in range(box_start_col, box_start_col + 3):
            if board[i][j] == num:
                return False

    return True

def find_empty_cell(board):
    
    # Finds an empty cell (with value 0) in the Sudoku board.
    
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def print_board(board):
    
    # Prints the Sudoku board in a readable format.
   
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def has_duplicates(lst):
    # Check if a list has any duplicates
    non_zeros = [x for x in lst if x != 0]
    return len(non_zeros) != len(set(non_zeros))

def check_sudoku_validity(board):
     # Check the Sudoku board for duplicates in rows, columns, and 3x3 blocks

     # Check each row and column
    if any(has_duplicates(board[i]) or has_duplicates([board[j][i] for j in range(9)]) for i in range(9)):
        return False

     # Check each 3x3 block
    if any(has_duplicates([board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]) for i in range(0, 9, 3) for j in range(0, 9, 3)):
        return False

    return True

def simple_progress_bar(total):
    for i in range(total + 1):
        percent = i / total * 100
        bar = "#" * (i // 5)
        print(f"\rSolving: [{bar:<20}] {percent:.1f}% ", end="")
        time.sleep(0.05)
    print("\n")

# Initial Sudoku board
sudoku_board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [0, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [0, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

print("\nOriginal Sudoku:\n")
print_board(sudoku_board)

# Check Sudoku validity before solving
if not check_sudoku_validity(sudoku_board):
    print("Invalid Sudoku: Duplicate values detected!")
else:
    total_iterations = 81  # Number of fields in sudoku
    simple_progress_bar(total_iterations)

    # Solve only if the Sudoku is valid
    if solve_sudoku(sudoku_board):
        print("\nSolved Sudoku:\n")
        print_board(sudoku_board)
    else:
        print("No solution found for this Sudoku!")