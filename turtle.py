'''now this thing shows you how to create or draw a square using turtle'''



import turtle
>>> t = turtle.Turtle()
>>> t.forward(100)
>>> t.left(90)
>>> t.forward(100)
>>> t.right(90)
>>> t.left(90)
>>> t.left(90)
>>> t.forward(100)
>>> t.left(90)
>>> t.forward(100)

#this is a program to print three circles using turtle
import turtle

def draw_circle(turtle, color, size, x, y):
    turtle.penup()
    '''turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(size)
    turtle.penup()
    turtle.end_fill()
    turtle.pendown()'''

tommy = turtle.Turtle()
tommy.shape("turtle")
tommy.speed(5)

draw_circle(tommy, "green", 50, 25, 0)
draw_circle(tommy, "blue", 50, 0, 0)
draw_circle(tommy, "yellow", 50, -25, 0)

tommy.penup()
tommy.goto(0,-50)
tommy.color('black')
tommy.write("Let's Learn Python!", align="center", font=(None, 16, "bold"))
tommy.goto(0,-80)


#this is using turtle for drawing a circle using a for loop
from turtle import *
for i in range(10000000):
    speed(1000)
    forward(150)
    right(95)


