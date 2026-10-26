WIDTH = 15
HEIGHT = 20
BORDER_SYMBOL = '#'



class Map:

    width: int
    height: int
    field: list[str]
    border: str

    def __init__(self,width=WIDTH,height=HEIGHT,border=BORDER_SYMBOL):
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


