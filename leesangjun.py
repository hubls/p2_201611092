#바람개비 모형 그리기 다이어그램 
3 %%plantuml 
4 @startuml
 
5 start 
6 :set size, bigger, sides, angle; 
7 repeat 
8 if (i is multiples of 2) then 
9     :size=existing size+bigger; 
10 endif 
11 :t1.fd(size); 
12 :t1.right(angle); 
13 repeat while(sides) 
14 stop 
15 @enduml 

#바람개비 모형
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
