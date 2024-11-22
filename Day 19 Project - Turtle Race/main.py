from turtle import Turtle, Screen
import random

is_race_on = False
color = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = [-70, -40, -10, 20, 50, 80]
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Choose your color: ")
all_turtles = []

if user_bet:
    is_race_on = True

    for turtle_index in range(0, 6):
        new_turtle = Turtle(shape='turtle')
        new_turtle.penup()
        new_turtle.color(color[turtle_index])
        new_turtle.goto(x=-230, y=y_positions[turtle_index])
        all_turtles.append(new_turtle)

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 210:
            is_race_on = False
            winning_color = (turtle.pencolor())
            if winning_color == user_bet:
                print(f"You've won. The {winning_color} turtle is the winner")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()