from Classes.Blocks import Door, Floor, Wall
import pickle

class Map:
    # инициализация
    def __init__(self, map_array):
        self.map_array = map_array

    #Генерирует карту. Создаёт объекты карты
    def CreateMap(self):

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

                # Если 2 - то есть пол
                if self.map_array[x][y] == 2:
                    mapRows.append(Floor(y, x, "Floor"))

                # Если 1 - то есть стенка
                elif self.map_array[x][y] == 1:

                    if rows - 1 > x > 0 and cols - 1 > y > 0:
                        if (self.map_array[x][y - 1] < 2 or self.map_array[x][y + 1] < 2) and self.map_array[x - 1][y] > 1 and self.map_array[x + 1][y] > 1:
                            mapRows.append(Wall(y, x, "Wall_Horizontal"))
                        elif self.map_array[x][y - 1] > 1 and self.map_array[x][y + 1] > 1 and (self.map_array[x - 1][y] < 2 or self.map_array[x + 1][y] < 2):
                            mapRows.append(Wall(y, x, "Wall_Vertical"))  
                        elif self.map_array[x][y - 1] > 1 and self.map_array[x][y + 1] < 2 and self.map_array[x - 1][y] > 1 and self.map_array[x + 1][y] < 2:
                            mapRows.append(Wall(y, x, "Wall_LeftUp"))  
                        elif self.map_array[x][y - 1] > 1 and self.map_array[x][y + 1] < 2 and self.map_array[x - 1][y] < 2 and self.map_array[x + 1][y] > 1:
                            mapRows.append(Wall(y, x, "Wall_LeftDown"))  
                        elif self.map_array[x][y - 1] < 2 and self.map_array[x][y + 1] > 1 and self.map_array[x - 1][y] > 1 and self.map_array[x + 1][y] < 2:
                            mapRows.append(Wall(y, x, "Wall_RightUp"))  
                        elif self.map_array[x][y - 1] < 2 and self.map_array[x][y + 1] > 1 and self.map_array[x - 1][y] < 2 and self.map_array[x + 1][y] > 1:
                            mapRows.append(Wall(y, x, "Wall_RightDown"))    
                        elif self.map_array[x][y - 1] < 2 and self.map_array[x][y + 1] < 2 and self.map_array[x - 1][y] < 2 and self.map_array[x + 1][y] > 1:
                            mapRows.append(Wall(y, x, "Wall_TriangularDown"))
                        elif self.map_array[x][y - 1] < 2 and self.map_array[x][y + 1] < 2 and self.map_array[x - 1][y] > 1 and self.map_array[x + 1][y] < 2:
                            mapRows.append(Wall(y, x, "Wall_TriangularUp"))
                        elif self.map_array[x][y - 1] > 1 and self.map_array[x][y + 1] < 2 and self.map_array[x - 1][y] < 2 and self.map_array[x + 1][y] < 2:
                            mapRows.append(Wall(y, x, "Wall_TriangularLeft"))
                        elif self.map_array[x][y - 1] < 2 and self.map_array[x][y + 1] > 1 and self.map_array[x - 1][y] < 2 and self.map_array[x + 1][y] < 2:
                            mapRows.append(Wall(y, x, "Wall_TriangularRight"))
                        elif self.map_array[x][y - 1] < 2 and self.map_array[x][y + 1] < 2 and self.map_array[x - 1][y] < 2 and self.map_array[x + 1][y] < 2:
                            mapRows.append(Wall(y, x, "Wall_Middle"))

                    elif x == rows - 1 and cols - 1 > y > 0:
                        if (self.map_array[x][y - 1] < 2 or self.map_array[x][y + 1] < 2) and self.map_array[x - 1][y] > 1:
                            mapRows.append(Wall(y, x, "Wall_Horizontal"))
                        elif self.map_array[x][y - 1] < 2 and self.map_array[x][y + 1] > 1 and self.map_array[x - 1][y] < 2:
                            mapRows.append(Wall(y, x, "Wall_RightDown"))
                        elif self.map_array[x][y - 1] > 1 and self.map_array[x][y + 1] < 2 and self.map_array[x - 1][y] < 2:
                            mapRows.append(Wall(y, x, "Wall_LeftDown"))
                        elif self.map_array[x][y - 1] < 2 and self.map_array[x][y + 1] < 2 and self.map_array[x - 1][y] < 2:
                            mapRows.append(Wall(y, x, "Wall_TriangularDown"))

                    elif rows - 1 > x > 0 and y == cols - 1:
                        if self.map_array[x][y - 1] > 1 and (self.map_array[x - 1][y] < 2 or self.map_array[x + 1][y] < 2):
                            mapRows.append(Wall(y, x, "Wall_Vertical"))
                        elif self.map_array[x][y - 1] < 2 and self.map_array[x - 1][y] < 2 and self.map_array[x + 1][y] > 1:
                            mapRows.append(Wall(y, x, "Wall_RightUp"))
                        elif self.map_array[x][y - 1] < 2 and self.map_array[x - 1][y] > 1 and self.map_array[x + 1][y] < 2:
                            mapRows.append(Wall(y, x, "Wall_RightDown"))
                        elif self.map_array[x][y - 1] < 2 and self.map_array[x - 1][y] < 2 and self.map_array[x + 1][y] < 2:
                            mapRows.append(Wall(y, x, "Wall_TriangularRight"))

                    elif x == 0 and cols - 1 > y > 0:
                        if (self.map_array[x][y - 1] < 2 or self.map_array[x][y + 1] < 2) and self.map_array[x + 1][y] > 1:
                            mapRows.append(Wall(y, x, "Wall_Horizontal"))
                        elif self.map_array[x][y - 1] < 2 and self.map_array[x][y + 1] > 1 and self.map_array[x + 1][y] < 2:
                            mapRows.append(Wall(y, x, "Wall_RightUp"))
                        elif self.map_array[x][y - 1] > 1 and self.map_array[x][y + 1] < 2 and self.map_array[x + 1][y] < 2:
                            mapRows.append(Wall(y, x, "Wall_LeftUp"))
                        elif self.map_array[x][y - 1] < 2 and self.map_array[x][y + 1] < 2 and self.map_array[x + 1][y] < 2:
                            mapRows.append(Wall(y, x, "Wall_TriangularUp"))

                    elif rows - 1 > x > 0 and y == 0:
                        if self.map_array[x][y + 1] > 1 and (self.map_array[x - 1][y] < 2 or self.map_array[x + 1][y] < 2):
                            mapRows.append(Wall(y, x, "Wall_Vertical"))
                        elif self.map_array[x][y + 1] < 2 and self.map_array[x - 1][y] < 2 and self.map_array[x + 1][y] > 1:
                            mapRows.append(Wall(y, x, "Wall_LeftDown"))
                        elif self.map_array[x][y + 1] < 2 and self.map_array[x - 1][y] > 1 and self.map_array[x + 1][y] < 2:
                            mapRows.append(Wall(y, x, "Wall_LeftUp"))
                        elif self.map_array[x][y + 1] < 2 and self.map_array[x - 1][y] < 2 and self.map_array[x + 1][y] < 2:
                            mapRows.append(Wall(y, x, "Wall_TriangularLeft"))

                    elif x == 0 and y == 0:
                        mapRows.append(Wall(y, x, "Wall_LeftUp"))

                    elif x == rows - 1 and y == cols - 1:
                        mapRows.append(Wall(y, x, "Wall_RightDown"))
                    
                    elif x == rows - 1 and y == 0:
                        mapRows.append(Wall(y, x, "Wall_LeftDown"))

                    elif x == 0 and y == cols - 1:
                        mapRows.append(Wall(y, x, "Wall_RightUp"))
                
                # Если 0 - то есть дверь
                elif self.map_array[x][y] == 0:
                    if self.map_array[x][y - 1] == 1 and self.map_array[x][y + 1] == 1:
                        mapRows.append(Door(y, x, "Door_Horizontal", 0))
                    elif self.map_array[x - 1][y] == 1 and self.map_array[x + 1][y] == 1:
                        mapRows.append(Door(y, x, "Door_Horizontal", 0))

            self.mapCols.append(mapRows)


    # Сохраняет карту, которая была построена по массиву
    def SaveMap(self, name):
        # Сохранение массива в файл
        with open('SaveMaps/' + name + '.pickle', 'wb') as file:
            pickle.dump(self.mapCols, file)


    # Загружает карту из файла, который был сохранён ранее
    def downloadMap(self, name):
        # Загрузка массива из файла
        with open('SaveMaps/' + name + '.pickle', 'rb') as file:
            self.mapCols = pickle.load(file)


    # Функция рисует карту (массив блоков)
    def draw(self, screen):
        for mapRows in self.mapCols:
            for block in mapRows:
                block.draw(screen)
        