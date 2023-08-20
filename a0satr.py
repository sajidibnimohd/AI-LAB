import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0
        self.h = 0

    def __lt__(self, other):
        return self.f() < other.f()

    def f(self):
        return self.g + self.h

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid, start, end):
    open_list = []
    closed_list = set()

    start_node = Node(start)
    end_node = Node(end)

    heapq.heappush(open_list, start_node)

    while len(open_list) > 0:
        current_node = heapq.heappop(open_list)
        closed_list.add(current_node.position)

        if current_node.position == end_node.position:
            path = []
            while current_node is not None:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        neighbors = []
        for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbor_position = (current_node.position[0] + move[0], current_node.position[1] + move[1])

            if neighbor_position[0] < 0 or neighbor_position[0] >= len(grid) or \
               neighbor_position[1] < 0 or neighbor_position[1] >= len(grid[0]) or \
               grid[neighbor_position[0]][neighbor_position[1]] == 1 or \
               neighbor_position in closed_list:
                continue

            neighbor = Node(neighbor_position, current_node)
            neighbor.g = current_node.g + 1
            neighbor.h = manhattan_distance(neighbor.position, end_node.position)

            if neighbor not in open_list:
                heapq.heappush(open_list, neighbor)

    return None

def create_grid(rows, cols):
    grid = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(int(input(f"Enter 0 for passable and 1 for obstacle at position ({i}, {j}): ")))
        grid.append(row)
    return grid

def get_coordinates():
    rows = int(input("Enter the number of rows in the grid: "))
    cols = int(input("Enter the number of columns in the grid: "))
    start_row = int(input("Enter the start row: "))
    start_col = int(input("Enter the start column: "))
    end_row = int(input("Enter the end row: "))
    end_col = int(input("Enter the end column: "))
    start = (start_row, start_col)
    end = (end_row, end_col)
    return rows, cols, start, end

def ao_star(grid, start, end):
    current_end = end
    path = a_star(grid, start, current_end)
    
    while True:
        if path[-1] == current_end:
            return path
        
        current_end = path[-1]
        path = a_star(grid, start, current_end)

if __name__ == "__main__":
    rows, cols, start, end = get_coordinates()
    grid = create_grid(rows, cols)

    path = ao_star(grid, start, end)
    if path:
        print("Shortest path found:")
        print(path)
    else:
        print("No path found.")
