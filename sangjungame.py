import turtle
wn=turtle.Screen()
d1=turtle.Turtle()
wn.bgcolor("green")
size=111

def Triangle():
 d1.penup()
 d1.goto(160,55)
 d1.pendown()
 for i in range(0,3):
  d1.fd(100)
  d1.right(120)

def Trianglea():
 d1.penup()
 d1.goto(-150,20)
 d1.pendown()
 for i in range(0,3):
  d1.fd(100)
  d1.right(120)

def Star():
	d1.penup()
	d1.setpos(-250,250)
	d1.pendown()
	for i in range(0,6):
		d1.fd(100)
		d1.right(144)

def Stara():
	d1.penup()
	d1.setpos(0,-250)
	d1.pendown()
	for i in range(0,6):
		d1.fd(100)
		d1.right(144)

Star()
Triangle()
Trianglea()

d1.penup()




from turtle import *

move = Turtle()
move.shape("turtle")
showturtle()
move.penup()

def k1():
    move.forward(45)

def k2():
    move.left(45)

def k3():
    move.right(45)

def k4():
    move.back(45)


onkey(k1, "Up")
onkey(k2, "Left")
onkey(k3, "Right")
onkey(k4, "Down")

listen()
mainloop()
