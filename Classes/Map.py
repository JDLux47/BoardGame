import pygame 
from Constants.Globals import BLOCK_SIZE
from Classes.Blocks import Wall, Empty
from Constants.Globals import BLOCK_SIZE

class Map:
    # инициализация
    def __init__(self, map_array):
        self.map_array = map_array

        # подсчёт строки столбцов в массиве карты
        rows = len(self.map_array)
        cols = len(self.map_array[0])
        print("Количество строк:", rows)
        print("Количество столбцов:", cols)

        # Создание объектов карты
        self.mapCols = [] # массив, который содежит строки блоков
        for x in range(rows):
            mapRows = [] # строки блоков
            for y in range(cols):
                if self.map_array[x][y] == 1:
                    mapRows.append(Wall(y, x))
                else:
                    mapRows.append(Empty(y, x))
                    
            self.mapCols.append(mapRows)

    # Функция рисует карту (массив блоков)
    def draw(self, screen):
        for mapRows in self.mapCols:
            for block in mapRows:
                block.draw(screen)
        