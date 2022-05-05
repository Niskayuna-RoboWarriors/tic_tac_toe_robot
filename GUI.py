import turtle as t
import Main.AI as AI

def init():
    screen=  t.getscreen()
    screen.screensize(800,800)
    t.hideturtle()
    t.speed(0)
    t.tracer(0,5) #changes screen refresh rate

def updateScreen():
    t.clear()

    colors=['black','white','red']
    square(-100,100,80,colors[AI.board[0]+1])
    square(0, 100, 80, colors[AI.board[1]+1])
    square(100, 100, 80, colors[AI.board[2]+1])
    square(0, 0, 80, colors[AI.board[3]+1])
    square(-100, 0, 80, colors[AI.board[4]+1])
    square(100, 0, 80, colors[AI.board[5]+1])
    square(-100, -100, 80, colors[AI.board[6]+1])
    square(0, -100, 80, colors[AI.board[7]+1])
    square(100, -100, 80, colors[AI.board[8]+1])


    t.update()

def square(x,y,size,color,rotation = 0):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(color)
    t.setheading(rotation)
    t.fillcolor(color)
    t.begin_fill()
    for a in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()
    t.penup()

init()
while True:
    updateScreen()

