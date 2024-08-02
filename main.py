import turtle
import random
import time

global x
global y
global counter

counter = 0
def make_screen():
    drawing_board = turtle.Screen()
    drawing_board.bgcolor("lightblue")

def make_title():
    game_title = turtle.Pen()
    game_title.pencolor("green")
    game_title.hideturtle()
    game_title.penup()
    game_title.setposition(-130,270)
    game_title.write("Catch the Turtle Game", font=("Verdana",17))


# positioning the turtle at random places and one-second intervals
def position_turtle(x,y):

    my_turtle = turtle.Turtle()
    my_turtle.color("green")
    my_turtle.shape("turtle")
    my_turtle.penup()
    my_turtle.speed(0)
    my_turtle.setposition(x,y)
    time.sleep(1)
    my_turtle.hideturtle()

# if the click is on the turtle 1 will write at the terminal, is it is not then o will write

def button_click(a,b):

    if a>x-8 and a<x+8 and b>y-8 and b<y+8:
        print(1)

    else:
        print(0)

# making background, writing game title and positioning the turtle at the origin

make_screen()
make_title()
position_turtle(0,0)

# the turtle will be positioned ten times at random places
while counter < 10:

    x = random.randint(-200, 200)
    y = random.randint(-200, 200)

    turtle.onscreenclick(button_click,1)
    turtle.listen()

    position_turtle(x,y)
    counter += 1

turtle.mainloop()
