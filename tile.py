from constants import *
import pygame


class Tile:

    def __init__(self, id:Blocks, row:int, col:int):
        self.id = id
        self.row = row
        self.col = col
        self.update_img()

    
    def draw(self, screen:pygame.surface.Surface):
        if self.id.value > Blocks.clear.value and self.id.value <= Blocks.start.value and self.id != Blocks.blob:
            self.update_img()
            screen.blit(self.img, (self.rect.x, self.rect.y))
        elif self.id == Blocks.blob:
            screen.blit(self.img, (self.rect.x, self.rect.y))
        else:
            self.rect = pygame.rect.Rect((self.col * TILE_WIDTH, self.row * TILE_HEIGHT,
                                          TILE_WIDTH, TILE_HEIGHT))

        
    def update_img(self):
        self.img = IMAGES[self.id.value - 1]
        self.rect = self.img.get_rect()
        if self.id == Blocks.start or self.id == Blocks.exit:
            padx = abs((TILE_WIDTH - self.img.get_width()) // 2)
            self.rect.x = self.col * TILE_WIDTH + (TILE_WIDTH - padx - self.img.get_width())
            pady = abs(2* TILE_HEIGHT - self.img.get_height())
            self.rect.y = (self.row - 1) * TILE_HEIGHT + pady
        elif self.id == Blocks.blob:
            self.rect.x = self.col * TILE_WIDTH
            self.rect.y = self.row * TILE_HEIGHT + 0.5 * TILE_HEIGHT
        else:
            self.rect.x = self.col * TILE_WIDTH
            self.rect.y = self.row * TILE_HEIGHT

    def is_clicked(self, pos) -> bool:      
        return self.rect.collidepoint(pos[0], pos[1])
    

    def __repr__(self) -> str:
        return f'Tile at {self.row}, {self.col} with id {self.id}'
    def __str__(self) -> str:
        return self.__repr__()

    
