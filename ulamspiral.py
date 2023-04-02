import turtle

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

sc = turtle.Screen()
sc.setup(500,500)
sc.bgcolor("black")

step = 1
size = 25
numsize = 1
state = 0
x = 0
y = 0
numstep = 1
turn = 0
num=1
t = turtle.Turtle()
t.color("white")
# t.penup()
while True:
    if(isPrime(num)):
        t.dot(10,"yellow")
    if(state==0):
        # x+=size
        t.goto(t.position()[0]+size,t.position()[1])
    elif(state==1):
        # y-=size
        t.goto(t.position()[0],t.position()[1]-size)
    elif(state==2):
        # x-=size
        t.goto(t.position()[0]-size,t.position()[1])
    else:
        y+=size
        t.goto(t.position()[0],t.position()[1]+size)
    if(step%numstep==0):
        state=(state+1)%4
        turn+=1
        if(turn%2==0):
            numstep+=1
    step+=1
    num+=1

turtle.done()