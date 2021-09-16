from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width = 500, height = 400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?  Enter a color: ")
print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles =[]

for turtle_index in range (0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You've won!  The {winning_color} turtle is the winner!")
            else:
                print("You've lost!  The {winning_color} turtle is the winner!")


        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)





###################################################################
# tim = Turtle(shape="turtle")
# tim.color(colors[0])
# tim.penup()
# tim.goto(x= -230, y = -75)
#
# tina = Turtle(shape="turtle")
# tina.color(colors[1])
# tina.penup()
# tina.goto(x= -230, y = -50)
#
# trish = Turtle(shape="turtle")
# tina.color(colors[2])
# trish.penup()
# trish.goto(x= -230, y = -25)
#
# terry = Turtle(shape="turtle")
# terry.color(colors[3])
# terry.penup()
# terry.goto(x= -230, y = 0)
#
# tom = Turtle(shape="turtle")
# tom.color(colors[4])
# tom.penup()
# tom.goto(x= -230, y = 25)
#
# tiberius = Turtle(shape="turtle")
# tiberius.color(colors[5])
# tiberius.penup()
# tiberius.goto(x= -230, y = 50)
#################################################################################

screen.exitonclick()







































# from turtle import Turtle, Screen
#
# tim = Turtle()
# screen = Screen()
# tim.speed("fastest")
#
#
# def move_forwards():
#    # tim.setheading(90)
#     tim.forward(10)
#
# def move_backwards():
#     #tim.setheading(270)
#     tim.forward(10)
#
# def move_left():
#     #tim.setheading(180)
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)
#
# def move_right():
#     #tim.setheading(0)
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)
#
# def clear_drawing():
#     screen.resetscreen()
#
# screen.listen()
# screen.onkey(key = "w", fun=move_forwards)
# screen.onkey(key = "s", fun=move_backwards)
# screen.onkey(key ="a", fun=move_left)
# screen.onkey(key = "d", fun= move_right)
# screen.onkey(key="c", fun=clear_drawing)
#
#
# screen.exitonclick()
#
#
#
#
#
