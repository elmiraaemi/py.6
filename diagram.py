from turtle import Turtle
t=Turtle()
t.shape('turtle')
t.speed(3)
x=25
y=-15
t.penup()
t.goto(x,y)
t.pendown()
for i in range (10):
    for j in range(i+3):
        t.left(360/(i+3))
        t.forward(50)
    x+=0.3
    y-=8
    t.penup()
    t.goto(x,y)
    t.pendown()