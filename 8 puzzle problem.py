from collections import deque

# Goal state
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

# Actions: left, right, up, down
actions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

# Function to get the next state by performing the given action
def get_next_state(state, action):
    new_state = state[:]
    empty_index = new_state.index(0)
    new_index = empty_index + action[0] * 3 + action[1]
    new_state[empty_index], new_state[new_index] = new_state[new_index], new_state[empty_index]
    return new_state

# Function to get the possible valid actions for the given state
def get_valid_actions(state):
    valid_actions = []
    empty_index = state.index(0)
    empty_row = empty_index // 3
    empty_col = empty_index % 3
    for action in actions:
        new_row = empty_row + action[0]
        new_col = empty_col + action[1]
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            valid_actions.append(action)
    return valid_actions

# Function to perform the Breadth-First Search
def bfs(initial_state):
    visited = set()
    queue = deque([(initial_state, [])])

    while queue:
        state, path = queue.popleft()
        visited.add(tuple(state))

        if state == goal_state:
            return path

        valid_actions = get_valid_actions(state)
        for action in valid_actions:
            next_state = get_next_state(state, action)
            if tuple(next_state) not in visited:
                queue.append((next_state, path + [action]))

    return None

# Function to get the initial state from user input
def get_initial_state():
    print("Enter the initial state of the puzzle (0 for empty tile):")
    initial_state = []
    for _ in range(3):
        row = list(map(int, input().split()))
        initial_state.extend(row)
    return initial_state

# Example usage
initial_state = get_initial_state()
solution = bfs(initial_state)
if solution:
    print("Solution found!")
    print("Number of steps:", len(solution))
    print("Path:", solution)
else:
    print("Solution not found!")

