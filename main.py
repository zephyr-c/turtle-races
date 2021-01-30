from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win? Enger a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

starting_line = -230
stall = -100

for c in colors:
    racer = Turtle(shape='turtle')
    racer.color(c)
    racer.pu()
    racer.goto(starting_line, stall)
    all_turtles.append(racer)
    stall += 30

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() >= 230:
            is_race_on = False
            print(f"The winner is the {turtle.pencolor()} turtle!")
            if user_bet == turtle.pencolor():
                print("You won!")
            else:
                print("Sorry, better luck next time!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()