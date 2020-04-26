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


#main game loop
while True:
    wn.update() #everytime the loop runs we update the screen.



