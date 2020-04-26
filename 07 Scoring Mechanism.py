'''
Pong
'''

#Allows python to do basic graphics
import turtle

#Create a window
wn = turtle.Screen()
wn.title("Pong by KD. A Game for Legends (aka 'old people')")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) #stop the window from updating so we have to update it

#Add Paddles and Ball
#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #set the paddle to the max possibly speed
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0) #set the paddle to the max possibly speed
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(+350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0) #set the paddle to the max possibly speed
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5 #everytime the ball moves it mvoes by 0.08 pixels. Faster computer need smaller numbers
ball.dy = -0.5

#Draw thw score on the screen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup() #we don't want to draw a line when the pen moves
pen.hideturtle #just want to see the text it is going to write
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

#Move Functions
# move paddle a up

def paddle_a_up():
    y = paddle_a.ycor() #from the turtle mod this returns the y co-ordinate
    y  += 20
    paddle_a.sety(y) #sets the new co-ordinate

# move paddle a down

def paddle_a_down():
    y = paddle_a.ycor() #from the turtle mod this returns the y co-ordinate
    y  -= 20
    paddle_a.sety(y) #sets the new co-ordinate

# move paddle b up
def paddle_b_up():
    y = paddle_b.ycor() #from the turtle mod this returns the y co-ordinate
    y  += 20
    paddle_b.sety(y) #sets the new co-ordinate

# move paddle b down

def paddle_b_down():
    y = paddle_b.ycor() #from the turtle mod this returns the y co-ordinate
    y  -= 20
    paddle_b.sety(y) #sets the new co-ordinate

#Keyboard binding
wn.listen() #listen for keyboard input
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#main game loop
while True:
    wn.update() #everytime the loop runs we update the screen.

    #Move the ball
    ball.setx(ball.xcor() + ball.dx) #ball moves 2 pixels at start of game
    ball.sety(ball.ycor() + ball.dy)

    # Border checks
    #top border
    if ball.ycor() > 290: #This is the top of the screen
        ball.sety(290)
        ball.dy *= -1 #this reverses the direction
    #bottom border
    if ball.ycor() < -290: #This is the Bottom of the screen
        ball.sety(-290)
        ball.dy *= -1

    #left border
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
    #Right border
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1

    #Collide paddle and ball by comparing the x and y positions of both
    #paddle and ball collisions
    #Right Paddle collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
    #Left Paddle collisions
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1