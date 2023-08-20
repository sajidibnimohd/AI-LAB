from collections import deque


# Function to check if the puzzle is solvable
def is_solvable(puzzle):
    inversions = count_inversions(puzzle)
    return inversions % 2 == 0

# Function to find the initial state that leads to an insolvable puzzle
def find_insolvable_state(initial_state, goal_state):
    visited = set()
    queue = deque([(initial_state, [])])

    while queue:
        current_state, path = queue.popleft()

        if current_state == goal_state:
            return path

        visited.add(tuple(map(tuple, current_state)))

        for move in get_possible_moves(current_state):
            if tuple(map(tuple, move)) not in visited:
                queue.append((move, path + [move]))

    return queue

# Function to find the index of the empty tile ('0') in the puzzle grid
def find_empty_tile(puzzle):
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == 0:
                return i, j

# Function to move the tiles in the puzzle grid and create a new state
def move_tile(puzzle, x1, y1, x2, y2):
    new_puzzle = [row[:] for row in puzzle]
    new_puzzle[x1][y1], new_puzzle[x2][y2] = new_puzzle[x2][y2], new_puzzle[x1][y1]
    return new_puzzle

# Function to check if the current puzzle state is the goal state
def is_goal(puzzle, goal_state):
    return puzzle == goal_state

# Function to get all possible moves from the current state
def get_possible_moves(puzzle):
    x, y = find_empty_tile(puzzle)
    moves = []
    if x > 0:
        moves.append(move_tile(puzzle, x, y, x - 1, y))
    if x < 2:
        moves.append(move_tile(puzzle, x, y, x + 1, y))
    if y > 0:
        moves.append(move_tile(puzzle, x, y, x, y - 1))
    if y < 2:
        moves.append(move_tile(puzzle, x, y, x, y + 1))
    return moves
def count_inversions(puzzle):
    inversions = 0
    flattened_puzzle = [cell for row in puzzle for cell in row if cell != 0]
    for i in range(len(flattened_puzzle)):
        for j in range(i + 1, len(flattened_puzzle)):
            if flattened_puzzle[i] > flattened_puzzle[j]:
                inversions += 1
    return inversions

# Breadth-First Search algorithm to solve the 8-puzzle problem
def bfs_solve(initial_state, goal_state):
    visited = set()
    queue = deque([(initial_state, [])])

    while queue:
        current_state, path = queue.popleft()

        if is_goal(current_state, goal_state):
            return path

        visited.add(tuple(map(tuple, current_state)))

        for move in get_possible_moves(current_state):
            if tuple(map(tuple, move)) not in visited:
                queue.append((move, path + [move]))

    return None

# Function to take the puzzle state as input from the user
def get_user_input():
    puzzle = []
    for _ in range(3):
        row = input().split()
        puzzle.append([int(cell) for cell in row])
    return puzzle

# # Example usage
# if __name__ == "__main__":
#     print("Enter the initial state (3x3 grid, use '0' for the empty tile):")
#     initial_state = get_user_input()

#     print("Enter the goal state (3x3 grid, use '0' for the empty tile):")
#     goal_state = get_user_input()

#     solution_path = bfs_solve(initial_state, goal_state)

#     if solution_path:
#         print("Solution Solvable:")
#         for step, state in enumerate(solution_path):
#             print(f"Step {step + 1}:")
#             for row in state:
#                 print(row)
#             print()
#     else:
#         print("Insolvable")



# Example usage
if __name__ == "__main__":
    print("Enter the initial state (3x3 grid, use '0' for the empty tile):")
    initial_state = get_user_input()

    print("Enter the goal state (3x3 grid, use '0' for the empty tile):")
    goal_state = get_user_input()
     

    if is_solvable(initial_state) and is_solvable(goal_state):
        solution_path = bfs_solve(initial_state, goal_state)

        if solution_path:
            print("Solution Solvable:")
            for step, state in enumerate(solution_path):
                print(f"Step {step + 1}:")
                for row in state:
                    print(row)
                print()
        else:
            print("No solution found.")
    else:
        print("Initial or goal state is unsolvable.")
        insolvable_steps = find_insolvable_state(initial_state, goal_state)
        if insolvable_steps:
            print("Steps to reach the insolvable state:")
            for step, state in enumerate(insolvable_steps):
                print(f"Step {step + 1}:")
                for row in state:
                    print(row)
                print()