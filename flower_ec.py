import random
from turtle import *
import math

# from pygments.formatters import oldmod

screen = Screen()
screen.bgcolor("white")


green_palette = ["springgreen","mediumspringgreen","lime","limegreen",
                 "lawngreen","chartreuse","greenyellow","palegreen",
                 "lightgreen","mediumseagreen","seagreen","yellowgreen",
                 "darkseagreen","lightseagreen","#00ff7f","#39ff14",
                 "#7fff00","#66ff66","#99ff66","#66ff99","#33ff99","#00ff99"]


class Flower(Turtle):
    def __init__(self,
                 x:int,
                 y:int,
                 petals:int,
                 size:int,
                 petal_color:str,
                 stamen_color:str,
                 stem_color:str = "green"):
        super().__init__()
        self._x = x
        self._y = y
        self._petals = petals
        self._size = size
        self._petal_color = petal_color
        self._stamen_color = stamen_color
        self._stem_color = stem_color

        self.hideturtle()
        self.speed(0)
        self.penup()

    def _draw_one_petal(self, shape: int = 60):
        self.begin_fill()
        self.color(self._petal_color)
        self.pensize(20)

        for _ in range(2):
            self.circle(self._size, shape)
            self.left(120)
        self.end_fill()

    def _draw_all_petals(self, shape: int = 60):
        for _ in range(self._petals):
            self.forward(self._size)
            self.pendown()
            self._draw_one_petal(shape)
            self.penup()
            self.goto(self._x, self._y)
            self.left(360/self._petals)

    def _draw_stamen(self):
        self.color(self._stamen_color)
        self.goto(self._x, self._y - self._size // 5)
        self.dot(self._size)

    def _draw_stem(self):
        self.penup()
        self.goto(self._x, self._y - self._size)
        self.color(self._stem_color)
        self.setheading(270)
        self.pensize(max(1, 15 - self._petals))
        self.pendown()
        self.forward(150)
        self.penup()
        print("flower complete")

    def draw_one_flower(self, shape:int = 60):
        self.goto(self._x, self._y)
        self.heading()
        self._draw_all_petals(shape)
        self._draw_stamen()
        self._draw_stem()


"""
                 x:int,
                 y:int,
                 petals:int,
                 size:int,
                 petal_color:str,
                 stamen_color:str,
                 stem_color:str = "green"
"""

rose = Flower(
        random.randint(-300, 300),
        random.randint(-300, 300),
        random.randint(6, 12),
        random.randint(5, 40),
        "red",
        "red",
        random.choice(green_palette)
)
rose.draw_one_flower(random.randint(30, 90))
tulip = Flower(
        random.randint(-300, 300),
        random.randint(-300, 300),
        random.randint(6, 12),
        random.randint(5, 40),
        "blue",
        "blue",
        random.choice(green_palette)
)
tulip.draw_one_flower(random.randint(30, 90))

daisy = Flower(
        random.randint(-300, 300),
        random.randint(-300, 300),
        random.randint(6, 12),
        random.randint(5, 40),
        "yellow",
        "white",
        random.choice(green_palette)
)
daisy.draw_one_flower(random.randint(30, 90))
lily = Flower(
        random.randint(-300, 300),
        random.randint(-300, 300),
        random.randint(6, 12),
        random.randint(5, 40),
        "purple",
        "purple",
        random.choice(green_palette)
)
lily.draw_one_flower(random.randint(30, 90))




mainloop()