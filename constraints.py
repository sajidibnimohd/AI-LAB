def print_board(board):
    for row in board:
        print(" ".join(str(num) for num in row))

def is_valid(board, row, col, num):
    # Check if 'num' is not in the same row, column, or 3x3 grid
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None, None

def certainty_satisfaction(board):
    row, col = find_empty_cell(board)
    if row is None:  # No empty cells left
        return True

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if certainty_satisfaction(board):
                return True

            board[row][col] = 0  # If the current placement doesn't lead to a solution, backtrack

    return False

def get_user_input():
    sudoku_board = []
    print("Enter the Sudoku puzzle (row by row):")
    for _ in range(9):
        row = input().split()
        row = [int(num) for num in row]
        sudoku_board.append(row)
    return sudoku_board

if __name__ == "__main__":
    user_input_board = get_user_input()

    if certainty_satisfaction(user_input_board):
        print("Sudoku solution:")
        print_board(user_input_board)
    else:
        print("No solution exists for the given Sudoku.")
