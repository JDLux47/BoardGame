import pygame
import json
from Classes.Map import Map
from Constants.Globals import SCREEN_HEIGHT, SCREEN_WIDTH
from Constants.Map_arrays import mapTest_array, map_array
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

# Создание поверхностей для двойного буфера
buffer_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
display_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

# создание карты
map = Map(mapTest_array)
map.CreateMap()
#map.downloadMap('Main')
map.SaveMap('Test')

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

    # Создаём поверхность, на которой рисуем карту или загружаем уже нарисованную
    buffer_surface.fill((0, 0, 0))  # Очистка буферной поверхности
    # buffer_surface = pygame.image.load("SaveMaps/Main.png")

    # отрисовывает карту на поверхности. Нужно для новых карт
    map.draw(buffer_surface)

    # Сохранение поверхности в файл. Для новых карт
    pygame.image.save(buffer_surface, "SaveMaps/Test.png")

    # Копирование буферной поверхности на отображаемую поверхность
    display_surface.blit(buffer_surface, (0, 0))

    # Отображение отображаемой поверхности на экране
    screen.blit(display_surface, (0, 0))

    # Обновление экрана
    pygame.display.flip()

# выходит из игры
pygame.quit()