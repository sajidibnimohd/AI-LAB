import pygame
import sys
import random
import heapq

# Constants
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Node:
    def __init__(self, pos, parent=None):
        self.pos = pos
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    def __lt__(self, other):
        return self.f < other.f

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(start, end, obstacle_positions):
    open_list = []
    closed_list = set()

    heapq.heappush(open_list, start)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_list.add(current_node.pos)

        if current_node.pos == end.pos:
            path = []
            while current_node:
                path.append(current_node.pos)
                current_node = current_node.parent
            return path[::-1]

        for direction in [UP, DOWN, LEFT, RIGHT]:
            neighbor_pos = (current_node.pos[0] + direction[0], current_node.pos[1] + direction[1])
            if neighbor_pos[0] < 0 or neighbor_pos[0] >= GRID_WIDTH or neighbor_pos[1] < 0 or neighbor_pos[1] >= GRID_HEIGHT:
                continue
            if neighbor_pos in obstacle_positions or neighbor_pos in closed_list:
                continue

            neighbor_node = Node(neighbor_pos, current_node)
            neighbor_node.g = current_node.g + 1
            neighbor_node.h = heuristic(neighbor_pos, end.pos)
            neighbor_node.f = neighbor_node.g + neighbor_node.h

            heapq.heappush(open_list, neighbor_node)

    return None

def generate_random_food(snake_positions):
    while True:
        x, y = random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)
        if (x, y) not in snake_positions:
            return x, y

def draw_grid(screen):
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(screen, WHITE, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, WHITE, (0, y), (WIDTH, y))

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")

    clock = pygame.time.Clock()

    snake_head = (GRID_WIDTH // 2, GRID_HEIGHT // 2)
    snake_positions = [snake_head]
    snake_direction = RIGHT
    food_pos = generate_random_food(snake_positions)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Handle key presses
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and snake_direction != DOWN:
            snake_direction = UP
        elif keys[pygame.K_DOWN] and snake_direction != UP:
            snake_direction = DOWN
        elif keys[pygame.K_LEFT] and snake_direction != RIGHT:
            snake_direction = LEFT
        elif keys[pygame.K_RIGHT] and snake_direction != LEFT:
            snake_direction = RIGHT

        # Move the snake
        new_head = (snake_head[0] + snake_direction[0], snake_head[1] + snake_direction[1])

        # Check for collision with the food
        if new_head == food_pos:
            food_pos = generate_random_food(snake_positions)
        else:
            snake_positions.pop()

        snake_head = new_head
        snake_positions.insert(0, snake_head)

        # Draw
        screen.fill((0, 0, 0))
        draw_grid(screen)

        # Draw the snake
        for segment in snake_positions:
            pygame.draw.rect(screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

        # Draw the food
        pygame.draw.rect(screen, RED, (food_pos[0] * GRID_SIZE, food_pos[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

        pygame.display.update()
        clock.tick(10)

if __name__ == "__main__":
    main()
