import pygame
from Constants.Globals import BLOCK_SIZE

from pygame.locals import (
    RLEACCEL,
)

class Block: 
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    
class Wall(Block):

    # инициализация
    def __init__(self, x, y):
        # берёт х и у от родителя
        super().__init__(x, y)
        self.image = pygame.image.load("Textures/wall.jpg").convert()
        # меняет размер изображения
        self.scaled_image = pygame.transform.scale(self.image, (BLOCK_SIZE, BLOCK_SIZE))

    # Функция рисует стену 
    def draw(self, screen):
        screen.blit(self.scaled_image, (self.x * BLOCK_SIZE, self.y * BLOCK_SIZE))


class Empty(Block):
    
    # инициализация
    def __init__(self, x, y):
        # берёт х и у от родителя
        super().__init__(x, y)
        self.image = pygame.image.load("Textures/empty.jpg").convert()
        # меняет размер изображения
        self.scaled_image = pygame.transform.scale(self.image, (BLOCK_SIZE, BLOCK_SIZE))

    # Функция рисует пустое место 
    def draw(self, screen):
        screen.blit(self.scaled_image, (self.x * BLOCK_SIZE, self.y * BLOCK_SIZE))