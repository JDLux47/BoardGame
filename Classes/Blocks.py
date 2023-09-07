import pygame
from Constants.Globals import BLOCK_SIZE

from pygame.locals import (
    RLEACCEL,
)


class Block: 
    
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name

    def draw(self, screen):
        self.image = pygame.image.load("Textures/" + self.name + ".png").convert()
        # меняет размер изображения
        self.scaled_image = pygame.transform.scale(self.image, (BLOCK_SIZE, BLOCK_SIZE))
        screen.blit(self.scaled_image, (self.x * BLOCK_SIZE, self.y * BLOCK_SIZE))


class Door(Block):

    def __init__(self, x, y, name, open):
        super().__init__(x, y, name) # берём атрибуты от родителя
        self.open = open
        
        # переопределяем метод draw для двери, потому что она может быть открыта или закрыта
    def draw(self, screen):   
        if self.name == "Door_Horizontal" and self.open == 1: # Если открыта и горизонтальная, то устанавливаем соответствующую текстуру 
            self.name = "DoorOpen_Horizontal"
        elif self.name == "Door_Vertical" and self.open == 1: # аналогично
            self.name = "DoorOpen_Vertical"
            
        self.image = pygame.image.load("Textures/" + self.name + ".png").convert() # Как у класса Block
        self.scaled_image = pygame.transform.scale(self.image, (BLOCK_SIZE, BLOCK_SIZE))
        screen.blit(self.scaled_image, (self.x * BLOCK_SIZE, self.y * BLOCK_SIZE))


class Wall(Block):

    def __init__(self, x, y, name):
        super().__init__(x, y, name)


class Floor(Block):

    def __init__(self, x, y, name):
        super().__init__(x, y, name)