sides=10
size=10
bigger=5
angle=90
def makeSwirlsquare(size,bigger,sides,angle):
    for i in range(0,sides):
        size=size+bigger
        t1.fd(size)
        t1.right(angle)
        
makeSwirlsquare(10,5,50,90)
