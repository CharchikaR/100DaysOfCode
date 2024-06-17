from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width=500, height=400)
user_turtle = screen.textinput(title="Pick you turtle", prompt="Which turtle do you pick? Enter color here: ")

is_race_on = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
y_start = -70
for x in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[x])
    new_turtle.penup()
    new_turtle.goto(-235, y_start)
    y_start += 30
    all_turtles.append(new_turtle)

if user_turtle:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_turtle:
                print(f"You've won! The winning turtle is {winning_color}!")
            else:
                print(f"You've lost! The winning turtle is {winning_color}!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)



screen.exitonclick()
