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
def lap7():
    global wn
    global t1
    import turtle
    wn=turtle.Screen()
    t1=turtle.Turtle()
    mytrack=drawSquareAt(100, (-100,100))
    print mytracks
    drawSquareFrom(100)


def main():
    lab7()
    
if __name__=="__main__":
    main()