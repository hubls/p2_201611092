﻿import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
t2=turtle.Turtle()


def DrawSquare(size,pos):
    t2.pencolor("Red")
    t2.penup()
    t2.goto(pos)
    t2.pendown()
    t2.fillcolor("Red")
    t2.begin_fill()
    for i in range(0,4):
        t2.fd(size)
        t2.right(90)
    t2.end_fill()
pos1=(-300,0)
size1=100
DrawSquare(size1,pos1)

def k1():
    t1.fd(50)
    (x,y)=t1.pos()
    global point
    if -300<=x<=-200 and -100<=y<=0:
        print "Game Over"
        t1.goto(0,0)
def k2():
    t1.left(15)

def k3():
    t1.right(15)

def k4():
    t1.back(10)

def mousegoto(x,y):
    t1.setpos(x,y)

    (x,y)=t1.pos()
    global point
    if -300<=x<=-200 and -100<=y<=0:
        print "Game Over"
        t1.goto(0,0)

def addmouse():
    wn.onclick(mousegoto)


def addkeys():
    wn.onkey(k1, "Up")
    wn.onkey(k2, "Left")
    wn.onkey(k3, "Right")
    wn.onkey(k4, "Down")


addkeys()
addmouse()
wn.listen()
turtle.mainloop()

