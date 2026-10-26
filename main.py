from enum import Enum



WIDTH = 15
HEIGHT = 20
BORDER_SYMBOL = '#'
TETRAMINO_SYMBOL = '*'

class Point:
    x: int
    y: int
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y


class Orientation(Enum):
    TOP = 'top'
    LEFT = 'left'
    BOTTOM = 'bottom'
    RIGHT = 'right'



class Figure(Enum):
    I = 'I'
    O = 'O'
    T = 'T'
    S = 'S'
    Z = 'Z'
    L = 'L'
    J = 'J'



class Tetramino:

    figure: Figure
    orientation: Orientation
    coords: list[Point]

    def __init__(self,figure: Figure, orientation: Orientation, x: int, y: int):
        self.figure = figure
        self.orientation = orientation
        
        match figure:
            case Figure.I:
                match orientation:
                    case Orientation.TOP:
                        pass
                    case Orientation.LEFT:
                        pass
                    case Orientation.BOTTOM:
                        pass
                    case Orientation.RIGHT:
                        pass
            case Figure.O:
                match orientation:
                    case Orientation.TOP:
                        pass
                    case Orientation.LEFT:
                        pass
                    case Orientation.BOTTOM:
                        pass
                    case Orientation.RIGHT:
                        pass
            case Figure.T:
                match orientation:
                    case Orientation.TOP:
                        pass
                    case Orientation.LEFT:
                        pass
                    case Orientation.BOTTOM:
                        pass
                    case Orientation.RIGHT:
                        pass
            case Figure.S:
                match orientation:
                    case Orientation.TOP:
                        pass
                    case Orientation.LEFT:
                        pass
                    case Orientation.BOTTOM:
                        pass
                    case Orientation.RIGHT:
                        pass
            case Figure.Z:
                match orientation:
                    case Orientation.TOP:
                        pass
                    case Orientation.LEFT:
                        pass
                    case Orientation.BOTTOM:
                        pass
                    case Orientation.RIGHT:
                        pass
            case Figure.L:
                match orientation:
                    case Orientation.TOP:
                        pass
                    case Orientation.LEFT:
                        pass
                    case Orientation.BOTTOM:
                        pass
                    case Orientation.RIGHT:
                        pass
            case Figure.J:
                match orientation:
                    case Orientation.TOP:
                        pass
                    case Orientation.LEFT:
                        pass
                    case Orientation.BOTTOM:
                        pass
                    case Orientation.RIGHT:
                        pass

    def rotate(self):
        pass

    def move_left(self):
        for point in self.coords:
            point.x += 1 

    def move_right(self):
        for point in self.coords:
            point.x -= 1 

    def fall(self):
        for point in self.coords:
            point.y += 1

class Map:

    width: int
    height: int
    field: list[str]
    tetramino: Tetramino

    def __init__(self,width:int = WIDTH, height:int = HEIGHT):
        self.width = width
        self.height = height
        self.field = []
        for i in range(height):
            if i==0 or i==height-1:
                self.field.append(BORDER_SYMBOL * width)
            else:
                self.field.append(BORDER_SYMBOL + " " * (width-2) + BORDER_SYMBOL)
   
    def add_tetramino_to_the_field(self, tetramino: Tetramino):
        if self.tetramino:
            for point in self.tetramino.coords:
                self.field[point.y][point.x] = ' '
            self.tetramino = tetramino                
        else:
            self.tetramino = tetramino
            for point in tetramino:
                self.field[point.y][point.x] = TETRAMINO_SYMBOL

    def drop_tetramino_from_field(self):
        if self.tetramino:
            for point in self.tetramino:
                self.field[point.y][point.x] = ' '

    def draw(self):
        if self.tetramino:
            self.drop_tetramino_from_field()
            for point in self.tetramino.coords:
                self.field[point.y][point.x] = TETRAMINO_SYMBOL
        for i in self.field:
            print(i)