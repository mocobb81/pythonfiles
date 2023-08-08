import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Game")

# Set up the game loop
clock = pygame.time.Clock()
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update game state
    # Here we randomly change the background color
    background_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    # Draw graphics
    screen.fill(background_color)
    
    # Update the display
    pygame.display.flip()
    
    # Delay the game loop to achieve a target framerate
    clock.tick(60)

# Quit Pygame
pygame.quit()
