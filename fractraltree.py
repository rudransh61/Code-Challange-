import turtle

sc = turtle.Screen()
sc.screensize(10000,10000)
sc.bgcolor("black")

t = turtle.Turtle()
t.color("white")
def tree(branchLen,t):
    if branchLen > 2:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-15,t)
        t.right(20)
        t.backward(branchLen)
t.left(90)
t.up()
t.backward(100)
t.down()
t.color("green")
tree(250,t)

turtle.done()