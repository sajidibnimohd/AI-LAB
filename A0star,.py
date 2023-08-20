import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    def __lt__(self, other):
        return self.f < other.f

def heuristic(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

def get_neighbors(current, grid):
    neighbors = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

    for dir_x, dir_y in directions:
        new_x = current[0] + dir_x
        new_y = current[1] + dir_y

        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == 0:
            neighbors.append((new_x, new_y))

    return neighbors

def a0star(grid, start, goal):
    open_list = []
    closed_set = set()

    start_node = Node(start)
    goal_node = Node(goal)

    heapq.heappush(open_list, start_node)

    while len(open_list) > 0:
        current_node = heapq.heappop(open_list)
        closed_set.add(current_node.position)

        if current_node.position == goal_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        neighbors = get_neighbors(current_node.position, grid)

        for neighbor_pos in neighbors:
            if neighbor_pos in closed_set:
                continue

            neighbor_node = Node(neighbor_pos, current_node)
            neighbor_node.g = current_node.g + 1
            neighbor_node.h = heuristic(neighbor_pos, goal_node.position)
            neighbor_node.f = neighbor_node.g + neighbor_node.h

            # Check if the neighbor is already in the open list and has a lower f value
            for open_node in open_list:
                if neighbor_pos == open_node.position and neighbor_node.g > open_node.g:
                    break
            else:
                heapq.heappush(open_list, neighbor_node)

    return None

def print_grid_with_path(grid, path):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) in path:
                print("*", end=" ")
            elif grid[i][j] == 1:
                print("#", end=" ")
            else:
                print(".", end=" ")
        print()

# Example usage with given inputs:
if __name__ == "__main__":
    # Define the grid
    grid = [
        [1, 0, 0, 0],
        [0, 1, 0, 2],
        [0, 0, 0, 1],
        [0, 0, 0, 0]
    ]

    # Define the start and goal positions
    start = (0, 1)
    goal = (0, 1)

    # Find the path using A0* algorithm
    path = a0star(grid, start, goal)

    if path:
        print("Path found:")
        print_grid_with_path(grid, path)
    else:
        print("No path found.")
