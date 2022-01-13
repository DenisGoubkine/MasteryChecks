# Pygame Cloud Function
"""
- Extract an x and y variable from the draw functions for the circles.
    - Choose one of the circle positions as x and y
    - Modify all other positions to relate to that x and y by subtracting and adding.
- Create the function. Have the function accept an x and y component and within the function
  draw the circles using those values.
- Call the function giving it the x and y values
- Call the function multiple times using differnt x and y values.
"""

import pygame
from pygame.constants import MOUSEBUTTONDOWN
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT

pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables



def cloud_function(x: int, y: int):
    pygame.draw.circle(screen, (255, 255, 255), (x, y), 30)
    pygame.draw.circle(screen, (255, 255, 255), (x+50, y+20), 30)
    pygame.draw.circle(screen, (255, 255, 255), (x-25, y+10), 30)
    pygame.draw.circle(screen, (255, 255, 255), (x+12, y+28), 30)
# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            print(event.pos)
    
    # GAME STATE UPDATES

    # DRAWING
    screen.fill((135, 206, 235)) 

    # cloud
    cloud_function(200, 200)
    cloud_function(100, 50)
    cloud_function(300, 100)

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()