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
ball.dx = 0.08 #everytime the ball moves it mvoes by 0.08 pixels. Faster computer need smaller numbers
ball.dy = 0.08

# ball x movement

# ball y movement

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
