from turtle import *
import turtle
#from turtle import *
t = turtle.Turtle()

def circle(f, a):
    t.forward(f)
    t.right(a)
    t.forward(f)
    t.right(a)
    t.forward(f)
    t.right(a)
    t.forward(f)
    t.right(a)
    t.forward(10)
    t.right(a+10)

#circle(100, 90)
#c = circle(100, 10)
for i in range(400):
    speed(5)
    circle(50, 50)
    

	
	
	
	
	
	
	
(#this is another program to perform squares out of circles)
	

	
	from turtle import *
import turtle
#from turtle import *
t = turtle.Turtle()

def circle(f, a):
    for loop in range(4):
        t.forward(f)
        t.right(a)
#circle(100, 90)
for j in range(100):
    speed(1000)
    circle(100, 90)
    t.right(10)
    #circle(100, 90)
