import turtle
import random

x_coordinates = [-200,-100,0,100,200]
y_coordinates = [-200,-100,0,100,200]
turtle_list = []
score = 0
game_over = False
screen = turtle.Screen()
screen.title("Catch the Turtle Game")
screen.bgcolor("light blue")

score_turtle = turtle.Turtle()

time_turtle = turtle.Turtle()
def write_score():

    score_turtle.hideturtle()
    score_turtle.penup()
    score_turtle.setpos(0, 290)
    score_turtle.write("Score 0",False, "center", ("arial", 18, "bold"))

def write_time(time):
    time_turtle.hideturtle()
    time_turtle.penup()
    time_turtle.setpos(0, 260)
    time_turtle.write("Time {}".format(time),False, "center", ("arial", 18, "bold"))

    if time>0:
        time_turtle.clear()
        time_turtle.write("Time {}".format(time), False, "center", ("arial", 18, "bold"))
        screen.ontimer(lambda: write_time(time-1),1000)
    else:
        global game_over
        game_over = True
        score_turtle.clear()
        time_turtle.clear()
        hide_turtles()
        time_turtle.setpos(0,15)
        score_turtle.setpos(0,-15)
        time_turtle.write("Game Over!", False, "center", ("arial", 25, "bold"))
        score_turtle.write("Your score is {}".format(score), False, "center",("arial", 25, "bold"))
def create_turtles():

    for x in x_coordinates:
        for y in y_coordinates:

            t = turtle.Turtle()

            def click_func(a,b):
                global score
                score += 1
                score_turtle.clear()
                score_turtle.write("Score {}".format(score), False, "center", ("arial", 18, "bold"))

            t.onclick(click_func)
            t.penup()
            t.shapesize(1.5, 1.5)
            t.color("green")
            t.shape("turtle")
            t.setposition(x,y)
            t.pendown()
            t.hideturtle()
            turtle_list.append(t)

def hide_turtles():
    for i in turtle_list:
        i.hideturtle()


def show_random_turtle():
    global game_over

    if game_over == False:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_random_turtle,1000)

turtle.tracer(0)

write_score()
write_time(15)

create_turtles()
show_random_turtle()

turtle.tracer(1)

turtle.mainloop()
