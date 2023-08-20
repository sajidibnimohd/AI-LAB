import random

# Board representation
board = [' ' for _ in range(9)]

# Winning combinations
winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]

# Heuristic evaluation for the board
def heuristic(board):
    score = 0
    for combo in winning_combinations:
        line = [board[i] for i in combo]
        if line.count('X') == 2 and line.count(' ') == 1:
            score += 1
        if line.count('O') == 2 and line.count(' ') == 1:
            score -= 1
    return score

# Check if the board is full
def is_board_full(board):
    return ' ' not in board

# Computer player's move using heuristic
def computer_move(board):
    best_move = -1
    best_eval = float('-inf')
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            eval = heuristic(board)
            board[i] = ' '
            if eval > best_eval:
                best_eval = eval
                best_move = i
    return best_move

# Main game loop
def main():
    print("Welcome to Tic-Tac-Toe!")
    print_board()
    
    while not is_board_full(board):
        player_move = int(input("Enter your move (0-8): "))
        if board[player_move] == ' ':
            board[player_move] = 'O'
        else:
            print("Invalid move. Try again.")
            continue
        
        print_board()
        
        if check_winner('O'):
            print("Congratulations! You win!")
            break
        
        if is_board_full(board):
            print("It's a draw!")
            break
        
        computer_move_index = computer_move(board)
        board[computer_move_index] = 'X'
        
        print_board()
        
        if check_winner('X'):
            print("Computer wins!")
            break

# Check if a player has won
def check_winner(player):
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

# Print the current state of the board
def print_board():
    for i in range(0, 9, 3):
        print(board[i], '|', board[i+1], '|', board[i+2])
        if i < 6:
            print('---------')

# Start the game
if __name__ == '__main__':
    main()
