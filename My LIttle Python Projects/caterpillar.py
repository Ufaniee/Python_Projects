import turtle as t
import random as rd
import time as ti

# create the bg color
t.bgcolor("light blue")

#create the labels
caterpillar=t.Turtle()
caterpillar.shape("square")
caterpillar.speed()
caterpillar.penup()
caterpillar.hideturtle()


leaf=t.Turtle()
leaf_shape=((0,0),(14,2),(18,6),(20,20),(6,18),(2,14))
t.register_shape("leaf",leaf_shape)
leaf.shape("leaf")
leaf.color("green")
leaf.penup()
leaf.speed()
leaf.hideturtle()

text_turtle= False
text_turtle=t.Turtle()
text_turtle.write("Press space to START", align="center", font=("Arial",18,"bold"))



score_turtle=t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

#define your functions
def outside_window():
    left_wall= t.window_width()/2   
    right_wall=t.window_width()/2
    top_wall=t.window_height()/2
    botttom_wall=t.window_height()/2
    (x,y)= caterpillar.pos()
    outside = x< left_wall or x > right_wall or y> top_wall or y < botttom_wall
    return outside

def place_leaf():
    leaf.hideturtle()
    leaf.setx(rd.randint(-200,200))
    leaf.sety(rd.randint(-200,200))
    leaf.showturtle()

def game_over():
    caterpillar.color("yellow")
    leaf.color('yellow')
    t.penup()
    t.hideturtle()
    t.write("GAME OVER", align="center",font=('Arial',30,'normal'))

def display_score(current_score):
    score_turtle.clear()
    score_turtle.penup()
    x=(t.window_width()/2) -50
    y=(t.window_height()/2)-50
    score_turtle.setposition(x,y)
    score_turtle.write(str(current_score),align='right', font=('Aerial',40,'bold'))

def start_game():
    global game_started
    if game_started:
        return
    game_started= True
    score = 0
    text_turtle.clear()

    caterpillar_speed = 2
    caterpillar_lenght = 3
    caterpillar.shapesize(1,caterpillar_lenght,1)
    caterpillar.showturtle()
    display_score(score)
    place_leaf()

    while True:
        caterpillar.forward(caterpillar.speed())
        if caterpillar.distance(leaf)< 5:
            place_leaf()
            caterpillar_lenght=caterpillar_lenght+1
            caterpillar_speed=caterpillar_speed+1
            score=score+10
            display_score(score)
        if outside_window():
            game_over()
            break



#def keys motion
def move_up():
    if caterpillar.heading() == 0 or caterpillar.heading()==180:
        caterpillar.setheading(90)
def move_down():
    if caterpillar.heading() == 0 or caterpillar.heading()==180:
        caterpillar.setheading(270)
def move_right():
    if caterpillar.heading() == 90 or caterpillar.heading()==270:
        caterpillar.setheading(0)
def move_left():
    if caterpillar.heading() == 90 or caterpillar.heading()==270:
        caterpillar.setheading(0)   


t.listen()
t.onkey(start_game,'space')
t.onkey( move_up,'Up')
t.onkey(move_down,'Down')
t.onkey(move_left,'Left')
t.onkey(move_right,'Right')

t.mainloop()




