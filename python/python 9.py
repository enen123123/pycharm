#棋盘
import turtle
a=300
t=turtle.Pen()
t.speed(0)
t.width(2)
t.color('pink')
for i in range(0,16):
    t.penup()
    t.goto(-300,a-i*30)
    t.pendown()
    t.goto(150,a-i*30)
for i in range(0,16):
    t.penup()
    t.goto(-a+i*30,300)
    t.pendown()
    t.goto(-a+30*i,-150)

turtle.done()


