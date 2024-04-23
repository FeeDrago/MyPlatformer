from constants import *
import pygame
from tile import Tile


class Blob(Tile, pygame.sprite.Sprite):

    def __init__(self, row, col):
        Tile.__init__(self, Blocks.blob, row, col)
        pygame.sprite.Sprite.__init__(self) 
        self.direction = Direction.right
        self.update_img()
        self.counter = 0

    def update_img(self):
        self.img = BLOB_IMG
        self.rect = self.img.get_rect()
        self.rect.x = self.col * TILE_WIDTH
        self.rect.y = self.row * TILE_HEIGHT + 0.5 * TILE_HEIGHT

    def __repr__(self) -> str:
        return f'Blob at {self.row}, {self.col} with id {self.id}'


    def update(self, tiles_list):
        # If at the end of the screen swap direction
        self.counter += 1
        if self.counter == 20:
            self.counter = 0
        if self.col == COLS - 1 and self.direction == Direction.right:
            self.direction = Direction.left
            self.rect.x -= BLOB_VEL_X
            return tiles_list
        elif self.col == 0 and self.direction == Direction.left:
            self.direction = Direction.right
            self.rect.x += BLOB_VEL_X
            return tiles_list
        
        # Check if the blob can continue moving in the current direction
        if self.direction == Direction.right:
            # if self.cols + 1 < COLS and self.row + 1 < ROWS:
            if tiles_list[self.row][self.col + 1].id == Blocks.clear and tiles_list[self.row + 1][self.col + 1].id != Blocks.clear and tiles_list[self.row + 1][self.col + 1].id != Blocks.lava:
                self.rect.x  += BLOB_VEL_X
                tiles_list[self.row][self.col + 1] = tiles_list[self.row][self.col]
                tiles_list[self.row][self.col] = Tile(Blocks.clear, self.row, self.col)
                self.col += 1
                return tiles_list
            else:
                self.direction = Direction.left
                return tiles_list

        elif self.direction == Direction.left:
            if self.col - 1 >= 0 and self.row + 1 < ROWS:
                # Check if moving left is possible and not at the beginning of the screen
                if tiles_list[self.row][self.col - 1].id == Blocks.clear and tiles_list[self.row + 1][self.col - 1].id != Blocks.clear and tiles_list[self.row + 1][self.col - 1].id != Blocks.lava:
                    self.rect.x -= BLOB_VEL_X  # Move left
                    tiles_list[self.row][self.col - 1] = tiles_list[self.row][self.col]
                    tiles_list[self.row][self.col] = Tile(Blocks.clear, self.row, self.col)
                    self.col -= 1
                    return tiles_list
                else:
                    self.direction = Direction.right  # Change direction to right if blocked
                    return tiles_list
        return tiles_list







