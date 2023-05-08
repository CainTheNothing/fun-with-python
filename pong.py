import turtle
import random

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Left Paddle
lpaddle = turtle.Turtle()
lpaddle.speed(0)
lpaddle.shape("square")
lpaddle.color("white")
lpaddle.shapesize(stretch_wid=5, stretch_len=1)
lpaddle.penup()
lpaddle.goto(-350, 0)

# Right Paddle
rpaddle = turtle.Turtle()
rpaddle.speed(0)
rpaddle.shape("square")
rpaddle.color("white")
rpaddle.shapesize(stretch_wid=5, stretch_len=1)
rpaddle.penup()
rpaddle.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.dx=random.choice([-.1, .1]) #move delta x by 2px , modify based on comp
ball.dy=random.choice([-.1, .1])

#Scoreboard
lscore=0
rscore=0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("P1: 0 P2: 0", align="center", font=("Courier", 24, "normal"))

#Movement
def lpaddle_up():
    lpaddle.sety(lpaddle.ycor() + 20)
def lpaddle_down():
    lpaddle.sety(lpaddle.ycor() - 20)
def rpaddle_up():
    rpaddle.sety(rpaddle.ycor() + 20)
def rpaddle_down():
    rpaddle.sety(rpaddle.ycor() - 20)

wn.listen()
wn.onkeypress(lpaddle_up, "w")
wn.onkeypress(lpaddle_down, "s")
wn.onkeypress(rpaddle_up, "Up")
wn.onkeypress(rpaddle_down, "Down")

while True:
    wn.update()

    #move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #paddle borders
    if rpaddle.ycor() > 250:
        rpaddle.goto(350, 250)
    if rpaddle.ycor() < -250:
        rpaddle.goto(350, -250)
    if lpaddle.ycor() > 250:
        lpaddle.goto(-350, 250)
    if lpaddle.ycor() < -250:
        lpaddle.goto(-350, -250)

    #ball border bounce and reset to center
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 #reverse direction

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 400:
        ball.goto(0,0)
        ball.dx *= random.choice([-1, 1])
        ball.dy *= random.choice([-1, 1])
        lscore += 1
        score.clear()
        score.write("P1: {} P2: {}".format(lscore, rscore), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -400:
        ball.goto(0,0)
        ball.dx *= random.choice([-1, 1])
        ball.dy *= random.choice([-1, 1])
        rscore += 1
        score.clear()
        score.write("P1: {} P2: {}".format(lscore, rscore), align="center", font=("Courier", 24, "normal"))

    #paddle/ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < rpaddle.ycor() + 40 and ball.ycor() > rpaddle.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < lpaddle.ycor() + 40 and ball.ycor() > lpaddle.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1