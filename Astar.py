import heapq

class Node:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    def __lt__(self, other):
        return self.f < other.f

def heuristic(current, goal):
    # Calculate the heuristic distance between two nodes
    return abs(ord(current.name) - ord(goal.name))

def trace_paths(current_node):
    path = []
    while current_node:
        path.append(current_node.name)
        current_node = current_node.parent
    return path[::-1]

def astar(adjacency_list, start, goal):
    open_set = []
    closed_set = set()
    start_node = Node(start)
    goal_node = Node(goal)
    heapq.heappush(open_set, start_node)
    all_paths = []  # Store all possible paths
    while open_set:
        current_node = heapq.heappop(open_set)
        if current_node.name == goal_node.name:
            update_all_paths(current_node, start_node, all_paths)
        closed_set.add(current_node.name)
        for neighbor, cost in adjacency_list[current_node.name]:
            if neighbor in closed_set:
                continue
            new_cost = current_node.g + cost
            if (
                neighbor not in [node.name for node in open_set]
                and neighbor not in closed_set
            ):
                neighbor_node = Node(neighbor, current_node)
                neighbor_node.g = new_cost
                neighbor_node.h = heuristic(neighbor_node, goal_node)
                neighbor_node.f = neighbor_node.g + neighbor_node.h
                heapq.heappush(open_set, neighbor_node)
            else:
                for node in open_set:
                    if node.name == neighbor and new_cost < node.g:
                        node.g = new_cost
                        node.f = node.g + node.h
                        node.parent = current_node

    return all_paths  # Return all the possible paths

def update_all_paths(current_node, start_node, all_paths):
    path = trace_paths(current_node)
    cost = current_node.g
    all_paths.append((path, cost))

def dfs(adjacency_list, current_node, goal_node, visited, path, all_paths):
    visited.add(current_node)
    if current_node == goal_node:
        all_paths.append(
            (path[:], path_cost(path, adjacency_list))
        )  # Append a copy of the path and its cost
        visited.remove(current_node)
        return
    for neighbor, cost in adjacency_list[current_node]:
        if neighbor not in visited:
            path.append(neighbor)
            dfs(adjacency_list, neighbor, goal_node, visited, path, all_paths)
            path.pop()
    visited.remove(current_node)

def path_cost(path, adjacency_list):
    total_cost = 0
    for i in range(len(path) - 1):
        current_node = path[i]
        next_node = path[i + 1]
        for neighbor, cost in adjacency_list[current_node]:
            if neighbor == next_node:
                total_cost += cost
    return total_cost

def find_all_paths(adjacency_list, start, goal):
    all_paths = []
    visited = set()
    path = [start]
    dfs(adjacency_list, start, goal, visited, path, all_paths)
    return all_paths

def print_all_paths(all_paths):
    print("\nAll possible paths:")
    for i, (path, cost) in enumerate(all_paths):
        print(f"Path {i + 1}: {' -> '.join(path)}, cost: {cost}")
    shortest_path, shortest_cost = min(all_paths, key=lambda x: x[1])
    print("\nShortest path:")
    print(" -> ".join(shortest_path), "\nCost:", shortest_cost)

adjacency_list = {}
num_nodes = int(input("Enter the number of nodes in the graph: "))
for _ in range(num_nodes):
    node = input("Enter node name: ")
    neighbors = input(
        f"Enter {node}'s neighbors and corresponding weights (separated by spaces): "
    ).split()
    neighbors = [
        (neighbors[i], int(neighbors[i + 1])) for i in range(0, len(neighbors), 2)
    ]
    adjacency_list[node] = neighbors
start_node = input("Enter the start node: ")
goal_node = input("Enter the goal node: ")
all_paths = find_all_paths(adjacency_list, start_node, goal_node)
if all_paths:
    print_all_paths(all_paths)
else:
    print("No path found.")

