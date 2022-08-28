#靶子
import turtle

t=turtle.Pen()
color=('black','red','yellow','pink''green')
t.width(30)#宽度
t.speed(0)#速度
for i in range(1,20):
    t.penup()
    t.goto(0, -10*i)
    t.pendown()
    t.color(color[i%3])
    t.circle(10*i)
turtle.done()