from constants import *
import pygame
from tile import Tile
import json
from pprint import pprint
from blob import Blob

class Level:
    def __init__(self, level_data: list=None):

        if level_data is None:
            level_data = [[0 for col in range(COLS)] for row in range(ROWS)]

        self.tiles_list = [[0 for col in range(COLS)] for row in range(ROWS)]


        for row_index, row in enumerate(level_data):
            for col_index, id in enumerate(row):
                if id != Blocks.blob.value:
                    self.tiles_list[row_index][col_index] = Tile(Blocks(id), row_index, col_index)
                else:
                    self.tiles_list[row_index][col_index] = Blob(row_index, col_index)

    def draw(self, screen, creator_mode=False):
        for row in self.tiles_list:
            for tile in row:

                if creator_mode:
                    tile.update_img()
                    tile.draw(screen)
                elif not creator_mode:
                    if tile.id == Blocks.blob:
                        if tile.counter < 20:
                            self.tiles_list = tile.update(self.tiles_list)
                        tile.draw(screen)
                    elif tile.id == Blocks.start:
                        continue
                    else:
                        tile.draw(screen)
                    

    def reset(self, screen):
        for row_index, row in enumerate(self.tiles_list):
            for col_index, id in enumerate(row):
                self.tiles_list[row_index][col_index] = Tile(Blocks(0), row_index, col_index)
        self.draw(screen=screen)

    @staticmethod
    def convert_tiles_list_to_list(tiles_list):
        return [[tile.id.value for tile in row] for row in tiles_list]



def save_level(level: Level, levels_loaded:bool, current_level:int):
    

    # Check if level has a start and exit door
    if check_level(level):
        # Read saved levels if any with int tile.id
        try:
            with open("levels.json", 'r') as f:
                data = f.read()
                if data:
                    old_levels = json.loads(data)
                else:
                    old_levels = {}
        except FileNotFoundError:
            old_levels = {}
        
        # Save it at the end
        if not levels_loaded:
            current_index = len(old_levels) + 1
            old_levels[current_index] = [[tile.id.value for tile in row] for row in level.tiles_list]


        # Edit the previous saved
        else:
            old_levels[current_level + 1] = [[tile.id.value for tile in row] for row in level.tiles_list]
        
        # Save
        with open("levels.json", 'w') as f:
            json.dump(old_levels, f)
    # Do nothing
    else:
        return

def load_all_levels():
    try:
        with open("levels.json", 'r') as f:
            levels_data = json.load(f)
            levels = []
            for index, level_data in levels_data.items():
                levels.append(Level(level_data=level_data))
    except (FileNotFoundError, json.JSONDecodeError):
        levels = []
    return levels

def load_level(level: Level, current_level: int, levels_loaded:bool) ->int:
    levels = load_all_levels()

    if len(levels) == 0: # Do nothing
        pass
    
    # If its the first time pressing the button load the last saved level
    if not levels_loaded: 
        if len(levels) > 0:
            current_level = len(levels) - 1
            level = levels[-1]
        else:
            current_level = 0
            level = Level()
    # If its not the first time pressing the button cycle levels
    elif levels_loaded:
        # Go back to the beggining if index is about to go out of range
        if current_level + 1 == len(levels): 
            level = levels[0]
            current_level = 0
        # Load next level
        elif current_level + 1 < len(levels): 
            current_level += 1
            level = levels[current_level]

    return current_level, level


def check_level(level: Level):
    # Check if there is a start and exit door
    start_door_placed = False
    exit_door_placed = False
    for row in level.tiles_list:
        for tile in row:
            if tile.id == Blocks.start:
                start_door_placed = True
            if tile.id == Blocks.exit:
                exit_door_placed = True
    return start_door_placed and  exit_door_placed


def locate_start_door(level: Level):
    if check_level(level):
        for row_index, row in enumerate(level.tiles_list):
            for col_index,tile in enumerate(row):
                if tile.id == Blocks.start:
                    return row_index, col_index
    else:
        return None, None

def locate_exit_door(level: Level):
    if check_level(level):
        for row_index, row in enumerate(level.tiles_list):
            for col_index,tile in enumerate(row):
                if tile.id == Blocks.exit:
                    return row_index, col_index
        else:
            return None, None
    
def locate_enemies(level: Level) -> list:
    # find all tiles that are object of class Blob
    enemies = []    
    for row in level.tiles_list:
        for tile in row:
            if isinstance(tile, Blob):
                enemies.append(tile)
    return enemies