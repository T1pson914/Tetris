from enum import Enum



WIDTH:int = 15
HEIGHT:int = 20
BORDER_SYMBOL:str = '#'
TETRAMINO_SYMBOL:str = '*'



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



class Movement(Enum):
    ROTATE = 'rotate'
    MOVE_LEFT = 'mv_l'
    MOVE_RIGHT = 'mv_r'
    FALL = 'fall'



class Tetramino:

    figure: Figure
    orientation: Orientation
    coords: list[Point] 

    def __init__(self,figure: Figure, orientation: Orientation, x: int, y: int) -> None:
        self.figure = figure
        self.orientation = orientation

        match figure:
            case Figure.I:
                match orientation:
                    case Orientation.TOP:
                        self.coords = [Point(x,y),Point(x,y+1),Point(x,y+2),Point(x,y-1)]
                    case Orientation.LEFT:
                        self.coords = [Point(x,y),Point(x-1,y),Point(x+1,y),Point(x+2,y)]
                    case Orientation.BOTTOM:
                        self.coords = [Point(x,y),Point(x,y+1),Point(x,y+2),Point(x,y-1)]
                    case Orientation.RIGHT:
                        self.coords = [Point(x,y),Point(x-1,y),Point(x+1,y),Point(x+2,y)]
            case Figure.O:
                match orientation:
                    case Orientation.TOP:
                        self.coords = [Point(x,y),Point(x-1,y),Point(x-1,y-1),Point(x,y-1)]
                    case Orientation.LEFT:
                        self.coords = [Point(x,y),Point(x-1,y),Point(x-1,y-1),Point(x,y-1)]
                    case Orientation.BOTTOM:
                        self.coords = [Point(x,y),Point(x-1,y),Point(x-1,y-1),Point(x,y-1)]
                    case Orientation.RIGHT:
                        self.coords = [Point(x,y),Point(x-1,y),Point(x-1,y-1),Point(x,y-1)]
            case Figure.T:
                match orientation:
                    case Orientation.TOP:
                        self.coords = [Point(x,y),Point(x-1,y),Point(x+1,y),Point(x,y+1)]
                    case Orientation.LEFT:
                        self.coords = [Point(x,y),Point(x-1,y),Point(x,y-1),Point(x,y+1)]
                    case Orientation.BOTTOM:
                        self.coords = [Point(x,y),Point(x-1,y),Point(x+1,y),Point(x,y-1)]
                    case Orientation.RIGHT:
                        self.coords = [Point(x,y),Point(x+1,y),Point(x,y-1),Point(x,y+1)]
            case Figure.S:
                match orientation:
                    case Orientation.TOP:
                        self.coords = [Point(),Point(),Point(),Point()]
                    case Orientation.LEFT:
                        self.coords = [Point(),Point(),Point(),Point()]
                    case Orientation.BOTTOM:
                        self.coords = [Point(),Point(),Point(),Point()]
                    case Orientation.RIGHT:
                        self.coords = [Point(),Point(),Point(),Point()]
            case Figure.Z:
                match orientation:
                    case Orientation.TOP:
                        self.coords = [Point(),Point(),Point(),Point()]
                    case Orientation.LEFT:
                        self.coords = [Point(),Point(),Point(),Point()]
                    case Orientation.BOTTOM:
                        self.coords = [Point(),Point(),Point(),Point()]
                    case Orientation.RIGHT:
                        self.coords = [Point(),Point(),Point(),Point()]
            case Figure.L:
                match orientation:
                    case Orientation.TOP:
                        self.coords = [Point(),Point(),Point(),Point()]
                    case Orientation.LEFT:
                        self.coords = [Point(),Point(),Point(),Point()]
                    case Orientation.BOTTOM:
                        self.coords = [Point(),Point(),Point(),Point()]
                    case Orientation.RIGHT:
                        self.coords = [Point(),Point(),Point(),Point()]
            case Figure.J:
                match orientation:
                    case Orientation.TOP:
                        self.coords = [Point(),Point(),Point(),Point()]
                    case Orientation.LEFT:
                        self.coords = [Point(),Point(),Point(),Point()]
                    case Orientation.BOTTOM:
                        self.coords = [Point(),Point(),Point(),Point()]
                    case Orientation.RIGHT:
                        self.coords = [Point(),Point(),Point(),Point()]



class Map:

    width: int
    height: int
    field: list[str]
    tetramino: Tetramino | None

    def __init__(self,width:int = WIDTH, height:int = HEIGHT) -> None:
        self.width = width
        self.height = height
        self.field = []
        for i in range(height):
            if i==0 or i==height-1:
                self.field.append([BORDER_SYMBOL] * self.width)
            else:
                self.field.append([BORDER_SYMBOL] + [" "] * (width-2) + [BORDER_SYMBOL])
   
    def add_tetramino_to_the_field(self, tetramino: Tetramino) -> None:
        self.tetramino = tetramino
        for point in tetramino.coords:
            self.field[point.y][point.x] = TETRAMINO_SYMBOL

    def drop_tetramino_from_field(self) -> None:
        for point in self.tetramino.coords:
            self.field[point.y][point.x] = ' '
        self.tetramino = None
    def rotate_tetramino(self) -> None:
        self.drop_tetramino_from_field()
        tetramino = self.tetramino
        orientation = None
        if tetramino.orientation == Orientation.TOP:
            orientation = Orientation.LEFT
        if tetramino.orientation == Orientation.LEFT:
            orientation = Orientation.BOTTOM
        if tetramino.orientation == Orientation.BOTTOM:
            orientation == Orientation.RIGHT
        if tetramino.orientation == Orientation.RIGHT:
            orientation == Orientation.TOP
        virtual_tetramino = Tetramino(
            figure=tetramino.figure,
            orientation=orientation,
            x=tetramino.coords[0].x,
            y=tetramino.coords[0].y,
        )
        for point in virtual_tetramino.coords:
            if self.field[point.y][point.x] == BORDER_SYMBOL or self.field[point.y][point.x] == TETRAMINO_SYMBOL:
                self.add_tetramino_to_the_field(tetramino)
                return
            else:
                self.tetramino = virtual_tetramino
                self.add_tetramino_to_the_field(virtual_tetramino)


    def move_tetramino_left(self) -> None:
        self.drop_tetramino_from_field()
        tetramino = self.tetramino
        virtual_tetramino = Tetramino(
            figure=tetramino.figure,
            orientation=tetramino.orientation,
            x=(tetramino.coords[0].x - 1),
            y=tetramino.coords[0].y
        )
        for point in virtual_tetramino.coords:
            if self.field[point.y][point.x] == BORDER_SYMBOL or self.field[point.y][point.x] == TETRAMINO_SYMBOL:
                self.add_tetramino_to_the_field(tetramino)
                return
            else:
                self.tetramino = virtual_tetramino
                self.add_tetramino_to_the_field(virtual_tetramino)

    def move_tetramino_right(self) -> None:
        tetramino = self.tetramino
        self.drop_tetramino_from_field()
        virtual_tetramino = Tetramino(
            figure=tetramino.figure,
            orientation=tetramino.orientation,
            x=(tetramino.coords[0].x + 1),
            y=tetramino.coords[0].y
        )
        for point in virtual_tetramino.coords:
            if self.field[point.y][point.x] == BORDER_SYMBOL or self.field[point.y][point.x] == TETRAMINO_SYMBOL:
                self.add_tetramino_to_the_field(tetramino)
                return
            else:
                self.tetramino = virtual_tetramino
                self.add_tetramino_to_the_field(virtual_tetramino)

    def tetramino_fall(self) -> None:
        self.drop_tetramino_from_field()
        tetramino = self.tetramino
        virtual_tetramino = Tetramino(
            figure=tetramino.figure,
            orientation=tetramino.orientation,
            x=tetramino.coords[0].x,
            y=(tetramino.coords[0].y + 1)
        )
        for point in virtual_tetramino.coords:
            if self.field[point.y][point.x] == BORDER_SYMBOL or self.field[point.y][point.x] == TETRAMINO_SYMBOL:
                self.add_tetramino_to_the_field(tetramino)
                return
            else:
                self.tetramino = virtual_tetramino
                self.add_tetramino_to_the_field(virtual_tetramino)

    def draw(self) -> None:
        for i in self.field:
            row = ''.join(i)
            print(row)    


m = Map()


t = Tetramino(Figure.T,Orientation.TOP,6,6)



m.add_tetramino_to_the_field(t)


m.draw()
m.move_tetramino_right()
m.move_tetramino_right()
m.move_tetramino_right()
m.move_tetramino_right()
m.draw()