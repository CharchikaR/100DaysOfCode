from turtle import Turtle, Screen
from random import choice

color_list = [(235, 243, 252), (198, 32, 13), (248, 25, 236), (40, 188, 76), (39, 69, 216), (238, 5, 227),
              (227, 49, 159), (29, 154, 40), (212, 15, 76), (17, 17, 153), (241, 161, 36), (195, 12, 16),
              (223, 120, 21), (68, 31, 10), (61, 8, 15), (223, 206, 141), (11, 62, 97), (219, 11, 159), (54, 229, 209),
              (19, 49, 21), (238, 216, 157), (79, 212, 74), (10, 238, 228), (73, 168, 212), (93, 198, 233),
              (65, 239, 231), (217, 51, 88)]

t = Turtle()
screen = Screen()
screen.screensize(1080, 960)

screen.colormode(255)
t.speed("fast")


def create_dots(x, y):
    t.sety(y)
    t.setx(x)
    for _ in range(10):
        t.forward(50)
        t.dot(20, choice(color_list))


t.penup()
t.hideturtle()
x_pos = -200
y_pos = -200

for _ in range(10):
    create_dots(x_pos, y_pos)
    x_pos = -200
    y_pos += 50

screen.exitonclick()
