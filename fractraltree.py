import math
import turtle

sc = turtle.Screen()
sc.screensize(400,400)
sc.bgcolor("black")

t = turtle.Turtle()
t.color("white")
def branch(x,y,angle):
    if(y!=0):
        t.lt(angle)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.lt(angle)
    t.fd(50)
    branch(x-50*math.sin(math.radians(angle)),y+50*math.cos(math.radians(angle)),30)

branch(0,0,90)

turtle.done()