import pygame
from constants import *



class Player:

    def __init__(self, x, y):
        self.images_right = PLAYER_IMAGES_RIGHT
        self.images_left = PLAYER_IMAGES_LEFT
        self.img_index = 0
        self.counter = 0
        self.direction = Direction(0)
        self.img = self.images_right[self.img_index]
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_y = 0
        self.jumped = False
        self.on_a_tile = False
        # self.rect.width = width
        # self.rect.height = height

    def draw(self, screen):
        screen.blit(self.img, (self.rect.x, self.rect.y))


    


    def update(self, screen, tiles_list):

        dx = 0
        dy = 0 
        walking_cd = 5

        # Handle Movement

        keys_pressed = pygame.key.get_pressed()

        # Make player only be able to jump when his feet are on a block and not in the air  
        for row in tiles_list:
            for tile in row:
                if tile.rect.colliderect(self.rect.x, self.rect.y + 1, self.img.get_width(), self.img.get_height()):
                    if tile.id != Blocks.clear: 
                        self.on_a_tile = True
                        break
                    else:
                        self.on_a_tile = False

        if keys_pressed[pygame.K_SPACE] and not self.jumped and self.vel_y <= 0 and self.on_a_tile:
            self.vel_y -= PLAYER_VEL_Y
            self.jumped = True
        if not keys_pressed[pygame.K_SPACE]:
            self.jumped = False
        if keys_pressed[pygame.K_LEFT]:
            dx = -PLAYER_VEL_X
            self.counter += 1
            self.direction = Direction.left
        if keys_pressed[pygame.K_RIGHT]:
            dx += PLAYER_VEL_X
            self.counter += 1
            self.direction = Direction.right

        
        


        # Add Gravity
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

        # Check For Collision

        # Screen Collision
        if self.rect.left + dx < 0 or self.rect.right + dx > WIDTH: 
            dx = 0
        if self.rect.top + dy < 0 or self.rect.bottom + dy > HEIGHT:
            dy = 0

        # Block Collision
        for row in tiles_list:
            for tile in row:
                # Make sure its not an air block or a door
                if tile.id != Blocks.clear and tile.id != Blocks.start and tile.id != Blocks.exit:
                    
                    # In X Axis
                    if tile.rect.colliderect(self.rect.x + dx, self.rect.y, self.img.get_width(), self.img.get_height()):
                        dx = 0

                    # In Y Axis
                    if tile.rect.colliderect(self.rect.x, self.rect.y + dy, self.img.get_width(), self.img.get_height()):
                        # Check if player is jumping
                        if self.vel_y < 0: # hit tile from below
                            dy = tile.rect.bottom - self.rect.top
                            self.vel_y = 0
                        # Check if player is falling
                        elif self.vel_y >= 0: # hit tile from below
                            dy = tile.rect.top - self.rect.bottom
                            self.vel_y = 0
        # Update Position
        self.rect.x += dx
        self.rect.y += dy

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            dy = 0


        # Add Walking Animation

        # Set static image if player lets go of the buttons
        if not keys_pressed[pygame.K_LEFT] and not keys_pressed[pygame.K_RIGHT]:
            self.img_index = 0
            self.counter = 0
            if self.direction == Direction.right:
                self.img = self.images_right[self.img_index]
            elif self.direction == Direction.left:
                self.img = self.images_left[self.img_index]
            self.direction = 0




        if self.counter > walking_cd:
            self.counter = 0
            self.img_index += 1
            if self.img_index >= len(self.images_right):
                self.img_index = 0
            if self.direction == Direction.right:
                self.img = self.images_right[self.img_index]
            elif self.direction == Direction.left:
                self.img = self.images_left[self.img_index]






        # Draw player
        self.draw(screen)