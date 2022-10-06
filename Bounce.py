#Bounce.py
#Joshua Bowen
#4/8/2021
#Last Update: 10/6/2022

import turtle
import random

#initialize screen
wn = turtle.Screen()
wn.bgcolor("Black")

#initialize the "ball" turtle
bounce = turtle.Turtle()
bounce.color("lightgreen")
bounce.speed(0)
bounce.shape("circle")

#initialize a turtle to draw the "box"
bound = turtle.Turtle()
bound.color("White")
bound.speed(0)
bound.width(10)
bound.ht()

#draw the "box"
bound.up()
bound.goto(-200,-200)
bound.down()
for i in range(4):
    bound.fd(400)
    bound.lt(90)

#this function should return the angle that the "ball"
#turtle needs to rotate by to "bounce" off a wall
def perfect_turn():
    #for now this function will just return 10 and have to be called multiple times
    #in the future I might be able to use the "ball" turtle's heading for a perfect angle
    return 10

#move the "ball" to a random location and set it to a randomg heading
bounce.up()
bounce.fd(random.randint(-200,200))
bounce.down()
bounce.lt(random.randrange(0,360))

#infinite while loop that runs the whole show
while True:
    #if the "ball" is in the "box" then move forward
    if bounce.xcor() < 200 and bounce.xcor() > -200 and bounce.ycor() < 200 and bounce.ycor()  > -200:
        bounce.fd(1)
    #otherwise, turn
    elif bounce.xcor() < 200 or bounce.xcor() > -200 or bounce.ycor() < 200 or bounce.ycor()  > -200:
        #in the future I should try and distinguish between right and left turns
        bounce.right(perfect_turn())
        bounce.fd(1)
