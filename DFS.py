class State:
    def __init__(self, jug1, jug2):
        self.jug1 = jug1
        self.jug2 = jug2

    def __str__(self):
        return f'({self.jug1}, {self.jug2})'

    def __eq__(self, other):
        return self.jug1 == other.jug1 and self.jug2 == other.jug2

    def __hash__(self):
        return hash((self.jug1, self.jug2))


def dfs(jug1_capacity, jug2_capacity, target):
    visited = set()
    stack = []
    initial_state = State(0, 0)
    stack.append((initial_state, []))

    while stack:
        current_state, path = stack.pop()
        if current_state in visited:
            continue

        visited.add(current_state)

        if current_state.jug1 == target or current_state.jug2 == target:
            path.append(str(current_state))
            return path

        # Fill jug1
        if current_state.jug1 < jug1_capacity:
            next_state = State(jug1_capacity, current_state.jug2)
            if next_state not in visited:
                stack.append((next_state, path + [str(current_state) + ' -> ' + str(next_state)]))

        # Fill jug2
        if current_state.jug2 < jug2_capacity:
            next_state = State(current_state.jug1, jug2_capacity)
            if next_state not in visited:
                stack.append((next_state, path + [str(current_state) + ' -> ' + str(next_state)]))

        # Empty jug1
        if current_state.jug1 > 0:
            next_state = State(0, current_state.jug2)
            if next_state not in visited:
                stack.append((next_state, path + [str(current_state) + ' -> ' + str(next_state)]))

        # Empty jug2
        if current_state.jug2 > 0:
            next_state = State(current_state.jug1, 0)
            if next_state not in visited:
                stack.append((next_state, path + [str(current_state) + ' -> ' + str(next_state)]))

        # Pour jug1 to jug2
        if current_state.jug1 > 0 and current_state.jug2 < jug2_capacity:
            pour_amount = min(current_state.jug1, jug2_capacity - current_state.jug2)
            next_state = State(current_state.jug1 - pour_amount, current_state.jug2 + pour_amount)
            if next_state not in visited:
                stack.append((next_state, path + [str(current_state) + ' -> ' + str(next_state)]))

        # Pour jug2 to jug1
        if current_state.jug2 > 0 and current_state.jug1 < jug1_capacity:
            pour_amount = min(current_state.jug2, jug1_capacity - current_state.jug1)
            next_state = State(current_state.jug1 + pour_amount, current_state.jug2 - pour_amount)
            if next_state not in visited:
                stack.append((next_state, path + [str(current_state) + ' -> ' + str(next_state)]))

    return None


# Take input from the user
jug1_capacity = int(input("Enter the capacity of jug 1: "))
jug2_capacity = int(input("Enter the capacity of jug 2: "))
target_amount = int(input("Enter the target amount: "))

solution = dfs(jug1_capacity, jug2_capacity, target_amount)
if solution:
    print(f"Solution found: {' , '.join(solution)}")
else:
    print("Un Solvable")