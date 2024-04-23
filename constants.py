import pygame
from enum import Enum, auto

import pygame.locals

# GAME
FPS = 60
WIDTH = 1000
HEIGHT  = 1000
ROWS = 20
COLS = 20
TILE_WIDTH = WIDTH // COLS
TILE_HEIGHT = HEIGHT // ROWS
NUM_OF_BUTTONS = 5
BUTTON_WIDTH = WIDTH // NUM_OF_BUTTONS
BUTTON_HEIGHT = TILE_HEIGHT
REL_BUTTON_WIDTH = BUTTON_WIDTH // TILE_WIDTH
FOOTER_HEIGHT = 3 * TILE_HEIGHT
FOOTER_WIDTH = WIDTH
PLAYER_HEIGHT = 1.5 * TILE_HEIGHT
PLAYER_WIDTH = 0.8 * TILE_WIDTH
PLAYER_VEL_X = 5
PLAYER_VEL_Y = 15
BLOB_VEL_X = 20
# COLORS
WHITE = (255, 255, 255)
GREEN = (29, 140, 65)
ORANGE = (199, 95, 30)


# GAME IMAGES
SUN_IMG = pygame.transform.scale(pygame.image.load("img/sun.png"), (WIDTH // 10, HEIGHT // 10))
SKY_IMG = pygame.transform.scale(pygame.image.load("img/sky.png"), (WIDTH, HEIGHT))
COIN_IMG = pygame.transform.scale(pygame.image.load("img/coin.png"), (TILE_WIDTH, TILE_HEIGHT))
DIRT_IMG =  pygame.transform.scale(pygame.image.load("img/dirt.png"), (TILE_WIDTH, TILE_HEIGHT))
LAVA_IMG = pygame.transform.scale(pygame.image.load("img/lava.png"), (TILE_WIDTH, TILE_HEIGHT))
GRASS_IMG =  pygame.transform.scale(pygame.image.load("img/grass.png"), (TILE_WIDTH, TILE_HEIGHT))
BLOB_IMG = pygame.transform.scale(pygame.image.load("img/blob.png"), (TILE_WIDTH, 0.5 * TILE_HEIGHT))
COIN_IMG = pygame.transform.scale(pygame.image.load("img/coin.png"), (TILE_WIDTH, TILE_HEIGHT))
GHOST_IMG = pygame.transform.scale(pygame.image.load("img/ghost.png"), (TILE_WIDTH * 0.8, TILE_HEIGHT * 1.6))
EXIT_IMG = pygame.transform.scale(pygame.image.load("img/exit.png"), (TILE_WIDTH * 0.8, TILE_HEIGHT * 1.6))
GUY1_IMG = pygame.transform.scale(pygame.image.load("img/guy1.png"), (0.8 * TILE_WIDTH, 1.6 * TILE_HEIGHT))
GUY2_IMG = pygame.transform.scale(pygame.image.load("img/guy2.png"), (0.8 * TILE_WIDTH, 1.6 * TILE_HEIGHT))
GUY3_IMG = pygame.transform.scale(pygame.image.load("img/guy3.png"), (0.8 * TILE_WIDTH, 1.6 * TILE_HEIGHT))
GUY4_IMG = pygame.transform.scale(pygame.image.load("img/guy4.png"), (0.8 * TILE_WIDTH, 1.6 * TILE_HEIGHT))
GUY1_IMG_LEFT = pygame.transform.flip(GUY1_IMG, True, False)
GUY2_IMG_LEFT = pygame.transform.flip(GUY2_IMG, True, False)
GUY3_IMG_LEFT = pygame.transform.flip(GUY3_IMG, True, False)
GUY4_IMG_LEFT = pygame.transform.flip(GUY4_IMG, True, False)
PLAYER_IMAGES_RIGHT = [GUY1_IMG, GUY2_IMG, GUY3_IMG, GUY4_IMG]
PLAYER_IMAGES_LEFT = [GUY1_IMG_LEFT, GUY2_IMG_LEFT, GUY3_IMG_LEFT, GUY4_IMG_LEFT]
PLATFORM_IMG =  pygame.transform.scale(pygame.image.load("img/platform.png"), (TILE_WIDTH, TILE_HEIGHT))
PLATFORM_X_IMG =  pygame.transform.scale(pygame.image.load("img/platform_x.png"), (TILE_WIDTH, TILE_HEIGHT))
PLATFORM_Y_IMG = pygame.transform.scale(pygame.image.load("img/platform_y.png"), (TILE_WIDTH, TILE_HEIGHT))
START_IMG = pygame.transform.scale(pygame.image.load("img/start.png"), (TILE_WIDTH * 0.8, TILE_HEIGHT * 1.6))
IMAGES = [DIRT_IMG, GRASS_IMG, LAVA_IMG, PLATFORM_IMG, PLATFORM_X_IMG, PLATFORM_Y_IMG, COIN_IMG,
           BLOB_IMG, EXIT_IMG, START_IMG]


# BUTTON IMAGES

EXIT_BUTTON_PNG = pygame.transform.scale(pygame.image.load("img/exit_btn.png"), (BUTTON_WIDTH, BUTTON_HEIGHT))
LOAD_BUTTON_PNG = pygame.transform.scale(pygame.image.load("img/load_btn.png"), (BUTTON_WIDTH, BUTTON_HEIGHT))
RESTART_BUTTON_PNG = pygame.transform.scale(pygame.image.load("img/restart_btn.png"), (BUTTON_WIDTH, BUTTON_HEIGHT))
SAVE_BUTTON_PNG = pygame.transform.scale(pygame.image.load("img/save_btn.png"), (BUTTON_WIDTH, BUTTON_HEIGHT))
START_BUTTON_PNG = pygame.transform.scale(pygame.image.load("img/start_btn.png"), (BUTTON_WIDTH, BUTTON_HEIGHT))
BUTTONS_IMAGES = {
    'save': SAVE_BUTTON_PNG,
    'restart': RESTART_BUTTON_PNG,
    'exit': EXIT_BUTTON_PNG,
    'load': LOAD_BUTTON_PNG,
    'start': START_BUTTON_PNG}




class Blocks(Enum):
    clear = 0
    dirt = 1
    grass = 2
    lava = 3
    platform = 4
    platform_x = 5
    platform_y = 6
    coin = 7
    blob = 8
    exit = 9
    start = 10

class Button_Type(Enum):
    save = 1
    restart = 2
    exit = 3
    load = 4
    start = 5

class Direction(Enum):
    right = 1
    left = -1
    standing = 0





