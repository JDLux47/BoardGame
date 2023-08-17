import pygame
import json
from Classes.Map import Map
from Constants.Globals import SCREEN_HEIGHT, SCREEN_WIDTH
from Constants.Map_arrays import mapTest_array
from Classes.Player import Player

#клавиши используемые в игре
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()

# настраивает окно отображения
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# создание карты
map = Map(mapTest_array)

# цикл игры
running = True

while running:

    # Просматривает события нажатий в очереди
    for event in pygame.event.get():
        # Проверка на нажатие клавиши
        if event.type == KEYDOWN:
            # Если нажат esc - выходит из игры
            if event.key == K_ESCAPE:
                running = False

        # Если нажата кнопка закрытия окна - завершает игру
        elif event.type == QUIT:
            running = False

    # Получает события нажатия клавиш
    pressed_keys = pygame.key.get_pressed()

    # Заполняет фон 
    screen.fill((0, 0, 0))

    # отрисовывает карту
    map.draw(screen)

    # Обновление экрана
    pygame.display.flip()

# выходит из игры
pygame.quit()