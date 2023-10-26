# Made by:
# Fernando García A01642285
# Federico Castro A01660986
# Diego Zepeda A01026512

import pygame
import sys

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


maze = [
    ["S", 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, "E"]
]


TILE_SIZE = 40
WINDOW_WIDTH = TILE_SIZE * len(maze[0])
WINDOW_HEIGHT = TILE_SIZE * len(maze)
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Maze Game")

player_pos = [0, 0]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    window.fill(WHITE)
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == 1:
                pygame.draw.rect(window, BLACK, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            elif maze[row][col] == "S" or maze[row][col] == "E":
                pygame.draw.rect(window, GREEN, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))
    
    pygame.draw.rect(window, BLUE, (player_pos[1] * TILE_SIZE, player_pos[0] * TILE_SIZE, TILE_SIZE, TILE_SIZE))
    
    pygame.display.flip()

pygame.quit()
sys.exit()

