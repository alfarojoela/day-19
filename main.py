from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.speed("fastest")


def move_forwards():
   # tim.setheading(90)
    tim.forward(10)

def move_backwards():
    #tim.setheading(270)
    tim.forward(10)

def move_left():
    #tim.setheading(180)
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def move_right():
    #tim.setheading(0)
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear_drawing():
    screen.resetscreen()

screen.listen()
screen.onkey(key = "w", fun=move_forwards)
screen.onkey(key = "s", fun=move_backwards)
screen.onkey(key ="a", fun=move_left)
screen.onkey(key = "d", fun= move_right)
screen.onkey(key="c", fun=clear_drawing)


screen.exitonclick()





