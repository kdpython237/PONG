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


#main game loop
while True:
    wn.update() #everytime the loop runs we update the screen.

