from enum import Enum



WIDTH = 15
HEIGHT = 20
BORDER_SYMBOL = '#'


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
    pass



class Map:

    width: int
    height: int
    field: list[str]
    border: str

    def __init__(self,width:int = WIDTH, height:int = HEIGHT, border:str = BORDER_SYMBOL):
        self.width = width
        self.height = height
        self.border = border
        self.field = []
        for i in range(height):
            if i==0 or i==height-1:
                self.field.append(self.border * width)
            else:
                self.field.append(self.border + " " * (width-2) + self.border)

    def draw(self):
        for column in self.field:
            print(column)
