import pygame
from constants import *
from level import Level, load_all_levels, locate_start_door
from tile import Tile
from button import Button
from player import Player
from blob import Blob

def draw_game_background(screen):
    # Background Images
    screen.blit(SKY_IMG, (0, 0))
    screen.blit(SUN_IMG, (100, 100))
    # Footer
    pygame.draw.rect(screen, ORANGE, (0, HEIGHT, FOOTER_WIDTH, FOOTER_HEIGHT))




def main_game(level:Level):
    running = True
    clock = pygame.time.Clock()
    row, col = locate_start_door(level)
    player = Player(col* TILE_WIDTH, row* TILE_HEIGHT)
    screen = pygame.display.set_mode((WIDTH, HEIGHT + FOOTER_HEIGHT))
    pygame.display.set_caption("My Platformer")
    



    while running:
        draw_game_background(screen=screen)
        level.draw(screen=screen)
        
        player.update(screen, level.tiles_list)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
        clock.tick(FPS)

if __name__ == '__main__':
    levels = load_all_levels()
    main_game(levels[0] if levels else Level())