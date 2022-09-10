import turtle

wind=turtle.Screen()#int screen
wind.title("ping pong")#set title
wind.bgcolor("black")#set the background
wind.setup(width=800, height=600)#set width and height
wind.tracer(0)#stop the window from update
#madrab1
madrab1=turtle.Turtle()
madrab1.speed(0)
madrab1.shape("square")
madrab1.color("blue")
madrab1.penup()
madrab1.goto(-350,0)
madrab1.shapesize(stretch_wid=5,stretch_len=1)
#madrab2
madrab2=turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("red")
madrab2.penup()
madrab2.goto(350,0)
madrab2.shapesize(stretch_wid=5,stretch_len=1)
#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.shapesize(stretch_wid=1,stretch_len=1)
ball.dx=0.04
ball.dy=-0.04
#functions
def madrab_up():
    y=madrab1.ycor()
    y+=20
    madrab1.sety(y)

def madrab_down():
    y=madrab1.ycor()
    y-=20
    madrab1.sety(y)

def madrab2_up():
    y=madrab2.ycor()
    y+=20
    madrab2.sety(y)

def madrab2_down():
    y=madrab2.ycor()
    y-=20
    madrab2.sety(y)  
#key
wind.listen()
wind.onkeypress(madrab_up,'w')
wind.onkeypress(madrab_down,'s')
wind.onkeypress(madrab2_up,'Up')
wind.onkeypress(madrab2_down,'Down')

while True:
    wind.update()
    #move
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    #border
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1
    elif ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1
    elif ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1
    elif ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx*=-1
    

