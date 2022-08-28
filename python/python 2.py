import turtle
import math

#定义点

x1,y1=0,50
x2,y2=50,0
x3,y3=0,-50
x4,y4=-50,0

#绘制
turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.goto(x2,y2)
turtle.goto(x3,y3)
turtle.goto(x4,y4)
turtle.goto(x1,y1)

#计算
distance=math.sqrt((x1-x2)**2+(y1-y2)**2)


turtle.write(distance)
