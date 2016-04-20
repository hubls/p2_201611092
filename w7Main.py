def drawSquareAt(size, pos): 
    t1.penup() 
    t1.setpos(pos) 
    t1.pendown()
    tracks=list()
    for i in range(0,4):
        tracks.append(t1.pos())
        t1.forward(size) 
        t1.right(90)
    return track

def drawSquareFrom(tracks):
    tracks=list()
    tracks.append((-100,-100))
    tracks.append((-100,100))
    tracks.append((100,-100))
    tracks.append((100,100))
    for i in range(0,4):
        drawSquareAt(100,tracks[i])
    
    def replaytracks(mytracks):
    for t in range(0,11):
        t1.goto(mytracks[t])
        
def lap7():
    global wn
    global t1
    import turtle
    wn=turtle.Screen()
    t1=turtle.Turtle()
    mytrack=drawSquareAt(100, (-100,100))
    print mytracks
    drawSquareFrom(100)
import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
t1.speed(5)
t1.penup()

mytracks=list()
t1.goto(-400,300)
mytracks.append(t1.pos())
t1.pendown()
t1.pencolor("Red")
t1.right(90)
t1.fd(400)
mytracks.append(t1.pos())
t1.backward(150)
mytracks.append(t1.pos())
t1.left(90)
t1.fd(300)
mytracks.append(t1.pos())
t1.left(90)
t1.fd(300)
mytracks.append(t1.pos())
t1.back(150)
mytracks.append(t1.pos())
t1.right(90)
t1.fd(300)
mytracks.append(t1.pos())
t1.left(90)
t1.right(90)
t1.right(90)
t1.fd(200)
mytracks.append(t1.pos())
t1.fd(300)
mytracks.append(t1.pos())
t1.back(100)
mytracks.append(t1.pos())
t1.left(90)
t1.fd(200)
mytracks.append(t1.pos())

replaytracks(mytracks)

def main():
    lab7()
    
if __name__=="__main__":
    main()
