#CS175L
#Conor Jacob
#stocks

import math
import turtle

# Named constants

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
ANIMATION_SPEED = 0
NUM_SIDES = 8
LENGTH = 100
ANGLE = 360/NUM_SIDES
TEXT_X = -5
TEXT_Y = -10

colors = ["red", "white" , "red"]
num_oct = 3
radius = LENGTH/(2*math.sin(math.pi/NUM_SIDES))
offset = 10 
startXCord =  -radius/2 + 15
startYCord =  -radius/2 - 35

turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
turtle.hideturtle()
turtle.penup()
turtle.goto(startXCord, startYCord)
turtle.pendown()
for i in range(num_oct):
    turtle.fillcolor(colors[i])
    turtle.begin_fill()
    for j in range(NUM_SIDES):
        turtle.forward(LENGTH)
        turtle.left(ANGLE)

    turtle.end_fill()
    x = turtle.xcor() + 5
    y = turtle.ycor() + offset
    LENGTH -=10
    radius = LENGTH/(2*math.sin(math.pi/NUM_SIDES))
        
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

turtle.penup()
turtle.goto(0, -10)
turtle.pendown()
turtle.color("white")
turtle.write("STOP", align = "center", font=("Arial", 30, "bold"))
turtle.done()




