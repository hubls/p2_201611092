def sumList(aList): 
    sum=0 
    for i in range(0,200): 
        sum=sum+aList[i] 
    return sum 

 
def lab6(): 
    aList=list() 
    for i in range(1,1001): 
        if i%4==0 and not i%5==0: 
            aList.append(i) 
    labsum=sumList(aList) 
    print labsum 
     
def main(): 
    lab6()
lab6()