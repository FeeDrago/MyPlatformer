import pygame
from constants import *
from level import *
from tile import Tile
from button import Button
from pprint import pprint
import sys
from game import main_game


pygame.init()


EXIT_EVENT = pygame.USEREVENT + 1
START_EVENT = pygame.USEREVENT + 2




def draw_background(screen, CURRENT_LEVEL_FONT, current_level, num_of_levels, levels_loaded:bool):
    screen.blit(SKY_IMG, (0, 0))
    screen.blit(SUN_IMG, (100, 100))
    current_level_text = CURRENT_LEVEL_FONT.render(f'Editing Level {current_level + 1}' + f"/{num_of_levels}"  if levels_loaded and num_of_levels >= 1 else "" ,1, WHITE)
    screen.blit(current_level_text, (WIDTH - current_level_text.get_width() - TILE_WIDTH, TILE_HEIGHT))

def create_buttons():
    buttons = {}

    # Save button
    buttons['save'] = Button(SAVE_BUTTON_PNG, 0 , HEIGHT, Button_Type.save)

    # Restart button
    buttons['restart'] = Button(RESTART_BUTTON_PNG, BUTTON_WIDTH, HEIGHT, Button_Type.restart)

    # Exit button
    buttons['exit'] = Button(EXIT_BUTTON_PNG, 2 * BUTTON_WIDTH, HEIGHT, Button_Type.exit)

    # Load button
    buttons['load'] = Button(LOAD_BUTTON_PNG, 3 * BUTTON_WIDTH, HEIGHT, Button_Type.load)
    
    # Start button
    buttons['start'] = Button(START_BUTTON_PNG, 4 * BUTTON_WIDTH, HEIGHT, Button_Type.start)

    return buttons

def draw_buttons(screen, buttons):
    for button in buttons.values():
        button.draw(screen)


def draw_grid(screen):
    # Horizontal Lines
    for row_index in range(ROWS):
        pygame.draw.line(screen, WHITE,(0, row_index * TILE_HEIGHT), (WIDTH, row_index * TILE_HEIGHT )) 
    # Vertical Lines
    for col_index in range(COLS):
        pygame.draw.line(screen, WHITE, (col_index * TILE_WIDTH, 0), (col_index * TILE_WIDTH, HEIGHT))

def level_creator():
    screen = pygame.display.set_mode((WIDTH, HEIGHT + TILE_HEIGHT))
    pygame.display.set_caption("Level Creator")
    CURRENT_LEVEL_FONT = pygame.font.SysFont('comicsans', 25)
    current_level = 0
    num_of_levels = len(load_all_levels())
    exit_door_placed = False
    start_door_placed = False
    running = True
    levels_loaded = False # Track if load btn has been pressed to know if it's supposed to edit a level or save it as new
    clock = pygame.time.Clock()
    level = Level()
    buttons = create_buttons()
    while running:
        draw_background(screen, CURRENT_LEVEL_FONT, current_level, num_of_levels, levels_loaded)
        draw_grid(screen=screen)
        draw_buttons(screen=screen, buttons=buttons)
        level.draw(screen=screen, creator_mode=True)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                # Left Click
                if event.button == 1:
                    # Cycle Block Type
                    for row in level.tiles_list:
                        for tile in row:
                            if tile.is_clicked(pos):
                                if tile.id.value < len(IMAGES):
                                    if tile.id.value + 1 == Blocks.exit.value and not exit_door_placed:
                                        exit_door_placed = True
                                        tile.id = Blocks(tile.id.value + 1)
                                    elif tile.id.value + 1 == Blocks.exit.value and exit_door_placed and not start_door_placed:
                                        tile.id = Blocks.start
                                        start_door_placed = True
                                    elif tile.id.value + 1 == Blocks.start.value and not start_door_placed:
                                        start_door_placed = True
                                        if tile.id == Blocks.exit:
                                            exit_door_placed = False
                                        tile.id = Blocks.start
                                    elif tile.id.value + 1 == Blocks.start.value and  start_door_placed and exit_door_placed:
                                        if tile.id == Blocks.exit:
                                            exit_door_placed = False
                                        tile.id = Blocks(0)
                                    elif tile.id.value + 1 == Blocks.exit.value and  start_door_placed and exit_door_placed:
                                        tile.id = Blocks(0)
                                    elif tile.id.value + 1 == Blocks.start.value and  not start_door_placed and  exit_door_placed:
                                        if tile.id == Blocks.exit:
                                            exit_door_placed = False
                                        tile.id = Blocks.start
                        

                                    elif tile.id.value + 1 == Blocks.start.value and start_door_placed:
                                        tile.id = Blocks(0)
                                    else:
                                        tile.id = Blocks(tile.id.value + 1)
                                else:
                                    if tile.id == Blocks.start:
                                        start_door_placed = False
                                    elif tile.id == Blocks.exit:
                                        exit_door_placed = False
                                    tile.id = Blocks(0)
                                
                    # Button pressed
                    for button in buttons.values():
                        if button.is_clicked(pos):
                            match button.id:
                                case Button_Type.save:
                                    save_level(level, levels_loaded, current_level)
                                case Button_Type.load:
                                    current_level, level = load_level(level, current_level, levels_loaded)
                                    levels_loaded = True
                                    start_pos = locate_start_door(level)
                                    exit_pos = locate_exit_door(level)
                                    if start_pos == (None, None):
                                        start_door_placed = False
                                    else:
                                        start_door_placed = True
                                    if exit_pos == (None, None):
                                        exit_door_placed = False
                                    else:
                                        exit_door_placed = True

                                case Button_Type.exit:
                                    running = False
                                    pygame.event.post(pygame.event.Event(EXIT_EVENT))
                                case Button_Type.restart:
                                    level.reset(screen=screen)
                                case Button_Type.start:
                                    running = False
                                    pygame.event.post(pygame.event.Event(START_EVENT))
                # Reset Block Type If right click clicked
                elif event.button == 3:
                    for row in level.tiles_list:
                        for tile in row:
                            if tile.is_clicked(pos):
                                if tile.id == Blocks.start:
                                    start_door_placed = False
                                elif tile.id == Blocks.exit:
                                    exit_door_placed = False
                                tile.id = Blocks(0)

        pygame.display.update()
        clock.tick(FPS)
    return level
    


if __name__ == '__main__':
    level = level_creator()
    for event in pygame.event.get():
        if event.type == EXIT_EVENT:
            pygame.quit()
            sys.exit()
        elif event.type == START_EVENT:
            main_game(Level(Level.convert_tiles_list_to_list(level.tiles_list)))