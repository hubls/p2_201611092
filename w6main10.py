def highlowgame():
    yourtrytime=0 
    x=input("input minimum") 
    y=input("input maximum") 
    USO=input("input user number one") 
    UST=input("input user number two") 

 
    if USO==UST:
             print "good!" 
   
    while UST!=USO: 
         
        if UST>=USO: 
                print "your number is High!" 
                UST=input("input user number two") 
                yourtrytime=yourtrytime+1 
         
        if UST<=USO: 
                print "your number is Low!" 
                UST=input("input user number two") 
                yourtrytime=yourtrytime+1 
         
        if USO==UST: 
             print "good!" 
         
    
     
         
    print "yourtrytime is "+str(yourtrytime)
highlowgame()