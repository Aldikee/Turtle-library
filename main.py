import turtle
import time
import math
turtle.bgcolor("light blue")

t = turtle.Turtle()
a = turtle.Turtle()
t.shape("square")
a.shape("turtle")
t.pensize(7)
a.pensize(5)

t.turtlesize(0.5, 0.5, 1)
a.turtlesize(0.5, 0.5, 1)

t.begin_fill()
t.fillcolor('green')
t.end_fill()


a.begin_fill()
a.fillcolor('green')
a.end_fill()

t.penup()
a.penup()#don't draw when turtle moves
t.goto(-300, 100)       #move the turtle to a location
a.goto(-300, -100)
t.pendown()
a.pendown()
ws = turtle.Screen() #создает окно для текстового запроса от пользователя

query = ""

def next(tur): #в конце каждый фигуры он добавлял отступ направо
    tur.penup()
    x, y = tur.pos()
    tur.goto(x + 130, y)
    tur.pendown()


while query != "stop":
    query = turtle.textinput("Shape", "Enter:")
    if query == "stop":
        t.write(" Hello World!")
        a.write(" I am turtle!")
        time.sleep(2)
    elif query == "quit":
        break
    elif query == "hexagon":
        t.begin_fill()
        t.fillcolor("black")
        for i in range(6):
            turtle.delay(10)
            t.forward(50)
            t.right(60)
        t.end_fill()
        next(t)

    elif query == "rhombus":
        t.begin_fill()
        t.fillcolor("red")
        t.left(50 // 2)
        t.forward(50)
        t.right(50)
        t.forward(50)
        t.right(180 - 50)
        t.forward(50)
        t.right(50)
        t.forward(50)
        t.right(360 - 205)
        t.end_fill()
        next(t)


    elif query == "ellipse":
        a.begin_fill()
        a.fillcolor("yellow")
        z = 75
        b = 45
        dx = a.xcor()
        dy = a.ycor()
        for deg in range(361):
            rad = math.radians(deg)
            x = z * math.sin(rad) + dx
            y = -b * math.cos(rad) + b + dy
            a.goto(x, y)
        a.end_fill()
        next(a)

    elif query == "triangle":
        a.begin_fill()
        a.fillcolor("blue")
        for i in range(3):
            turtle.delay(11)
            a.forward(50)
            a.left(120)
            a.forward(50)
        a.end_fill()
        next(a)
