import pygame
import sys
import random
import math

# init
pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


# const colors

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


#gmae loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    screen.fill(BLACK)
    pygame.display.flip()
    clock.tick(60)


pygame.quit()
sys.exit()