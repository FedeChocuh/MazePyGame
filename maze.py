import pygame
import sys

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

maze = [
    ["S", 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, "E"]
]


TILE_SIZE = 40
WINDOW_WIDTH = TILE_SIZE * len(maze[0])
WINDOW_HEIGHT = TILE_SIZE * len(maze)
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Maze Game")

player_pos = [0, 0] 



def is_game_over(pos):
    return maze[pos[0]][pos[1]] == 1

def is_game_won(pos):
    return maze[pos[0]][pos[1]] == "E"

running = True
game_over = False
game_won = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and not game_over and not game_won:
            if event.key == pygame.K_UP:
                if player_pos[0] > 0:
                    player_pos[0] -= 1
            elif event.key == pygame.K_DOWN:
                if player_pos[0] < len(maze) - 1:
                    player_pos[0] += 1
            elif event.key == pygame.K_LEFT:
                if player_pos[1] > 0:
                    player_pos[1] -= 1
            elif event.key == pygame.K_RIGHT:
                if player_pos[1] < len(maze[0]) - 1:
                    player_pos[1] += 1

            if is_game_over(player_pos):
                game_over = True
            if is_game_won(player_pos):
                game_won = True
    window.fill(WHITE)
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == 1:
                pygame.draw.rect(window, BLACK, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            elif maze[row][col] == "S" or maze[row][col] == "E":
                pygame.draw.rect(window, GREEN, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    if not game_over and not game_won:
        pygame.draw.rect(window, BLUE, (player_pos[1] * TILE_SIZE, player_pos[0] * TILE_SIZE, TILE_SIZE, TILE_SIZE))
    elif game_over:
        font = pygame.font.SysFont(None, 55)
        text = font.render("Game Over", True, RED)
        window.blit(text, (WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT // 2 - 30))
    elif game_won:
        font = pygame.font.SysFont(None, 55)
        text = font.render("You Win!", True, GREEN)
        window.blit(text, (WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT // 2 - 30))
    
    pygame.display.flip()

pygame.quit()
sys.exit()
