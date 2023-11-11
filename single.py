import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 700, 600
SNAKE_SIZE = 20
SPEED = 10

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Create the window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake initial position and direction
snake = [(100, 50), (90, 50), (80, 50)]
snake_direction = (SNAKE_SIZE, 0)

# Food initial position
food = (random.randrange(1, (WIDTH//SNAKE_SIZE)) * SNAKE_SIZE,
        random.randrange(1, (HEIGHT//SNAKE_SIZE)) * SNAKE_SIZE)

# Score
score = 0

# Game over flag
game_over = False

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Handle key presses
    keys = pygame.key.get_pressed()
    for key in keys:
        if keys[pygame.K_UP]:
            snake_direction = (0, -SNAKE_SIZE)
        if keys[pygame.K_DOWN]:
            snake_direction = (0, SNAKE_SIZE)
        if keys[pygame.K_LEFT]:
            snake_direction = (-SNAKE_SIZE, 0)
        if keys[pygame.K_RIGHT]:
            snake_direction = (SNAKE_SIZE, 0)

    # Move the snake
    new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
    snake.insert(0, new_head)

    # Check if the snake ate the food
    if snake[0] == food:
        score += 1
        food = (random.randrange(1, (WIDTH//SNAKE_SIZE)) * SNAKE_SIZE,
                random.randrange(1, (HEIGHT//SNAKE_SIZE)) * SNAKE_SIZE)
    else:
        snake.pop()

    # Check for collisions with the window edges
    if (snake[0][0] < 0 or snake[0][0] >= WIDTH or
            snake[0][1] < 0 or snake[0][1] >= HEIGHT):
        game_over = True

    # Check for collisions with itself
    if snake[0] in snake[1:]:
        game_over = True

    # Draw everything
    window.fill(WHITE)
    for segment in snake:
        pygame.draw.rect(window, GREEN, (segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))
    pygame.draw.rect(window, GREEN, (food[0], food[1], SNAKE_SIZE, SNAKE_SIZE))

    pygame.display.update()

    # Control the game speed
    pygame.time.Clock().tick(SPEED)

# Game over message
font = pygame.font.Font(None, 36)
game_over_text = font.render(f"Game Over - Your Score: {score}", True, GREEN)
window.blit(game_over_text, (WIDTH // 4, HEIGHT // 2))
pygame.display.update()

# Wait for a moment and then exit
pygame.time.delay(2000)
sys.exit()
