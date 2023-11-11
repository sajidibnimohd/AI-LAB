class State:
    def __init__(self, jug1, jug2):
        self.jug1 = jug1
        self.jug2 = jug2

    def __str__(self):
        return f"jug1: {self.jug1}  jug2: {self.jug2}"

    def __eq__(self, other):
        return self.jug1 == other.jug1 and self.jug2 == other.jug2

    def __hash__(self):
        return hash((self.jug1, self.jug2))

def dfs(jug1_capacity, jug2_capacity, target):
    visited = set()
    stack = []
    initial_state = State(0, 0)
    stack.append((initial_state, []))
    all_steps = []

    while stack:
        current_state, path = stack.pop()
        if current_state in visited:
            continue
        visited.add(current_state)
        all_steps.append((current_state, path))

        if current_state.jug1 == target or current_state.jug2 == target:
            path.append(str(current_state))
            return path, all_steps

        if current_state.jug1 < jug1_capacity:
            next_state = State(jug1_capacity, current_state.jug2)
            if next_state not in visited:
                stack.append((next_state, path + [str(current_state) + ' -> ' + str(next_state)]))

        if current_state.jug2 < jug2_capacity:
            next_state = State(current_state.jug1, jug2_capacity)
            if next_state not in visited:
                stack.append((next_state, path + [str(current_state) + ' -> ' + str(next_state)]))

        if current_state.jug1 > 0:
            next_state = State(0, current_state.jug2)
            if next_state not in visited:
                stack.append((next_state, path + [str(current_state) + ' -> ' + str(next_state)]))

        if current_state.jug2 > 0:
            next_state = State(current_state.jug1, 0)
            if next_state not in visited:
                stack.append((next_state, path + [str(current_state) + ' -> ' + str(next_state)]))

        pour_amount = min(current_state.jug1, jug2_capacity - current_state.jug2)
        if current_state.jug1 > 0 and current_state.jug2 < jug2_capacity:
            next_state = State(current_state.jug1 - pour_amount, current_state.jug2 + pour_amount)
            if next_state not in visited:
                stack.append((next_state, path + [str(current_state) + ' -> ' + str(next_state)]))

        pour_amount = min(current_state.jug2, jug1_capacity - current_state.jug1)
        if current_state.jug2 > 0 and current_state.jug1 < jug1_capacity:
            next_state = State(current_state.jug1 + pour_amount, current_state.jug2 - pour_amount)
            if next_state not in visited:
                stack.append((next_state, path + [str(current_state) + ' -> ' + str(next_state)]))

    last_step = (current_state, path)
    return None, all_steps

def print_solution(solution):
    print("Solution found:")
    for step in solution:
        print(step)

def print_all_steps(all_steps):
    print("All steps taken during DFS:")
    for i, (state, path) in enumerate(all_steps, start=1):
        print(f"Step {i}:")
        print(state)

# Take input from the user
jug1_capacity = int(input("Enter the capacity of jug 1: "))
jug2_capacity = int(input("Enter the capacity of jug 2: "))
target_amount = int(input("Enter the target amount: "))
solution, all_steps = dfs(jug1_capacity, jug2_capacity, target_amount)

if solution:
    print_solution(solution)
else:
    print("No solution found.")

print("The solution cannot proceed further after the following steps:")
# Print all steps, including the steps where the solution cannot proceed further
print_all_steps(all_steps)
