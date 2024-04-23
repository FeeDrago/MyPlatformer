from constants import *
import pygame


class Button:

    def __init__(self, img, x, y,id:Button_Type):
        self.img = img
        self.rect = img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.id = id
        

    def draw(self, screen):
        screen.blit(self.img, (self.rect.x, self.rect.y))
    
    def is_clicked(self, pos) -> bool:      
        return self.rect.collidepoint(pos[0], pos[1])
    