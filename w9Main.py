﻿def charCount(): 
    sentence='sangmyung university' 
    print list(sentence) 
    allchars= list(sentence) 
    for c in allchars: 
        print c, 
    d=dict() 
    for c in allchars: 
        if c not in d: 
            d[c]=1 
        else : 
            d[c]=d[c]+1 
    print d 
    import matplotlib 
    import matplotlib.pyplot as plt 

 
    plt.bar(range(len(d)),d.values(), align='center') 
    plt.xticks(range(len(d)), list(d.keys())) 
    plt.show() 

 
def countDigitsLetter(word): 
    sentence="7 hongjidong" 
    allchars= list(sentence) 
    d=dict() 
    d={"number":0, "word":0} 
    for c in word: 
        if c.isdigit()==True: 
            d["number"]=d["number"]+1 
        elif c.isdigit()==False: 
            d["word"]=d["word"]+1 

 
    print d 

 
    import matplotlib 
    import matplotlib.pyplot as plt 
    plt.bar(range(len(d)),d.values(), align='center') 
    plt.xticks(range(len(d)), list(d.keys())) 
    plt.show() 

 

 
myhome=set() 
yourhome=set() 
myhome={'TV','phone','camera','fridger','mixer','audio','cd','light','computer','notebook','recorder'} 
yourhome={'coffee','radio','camera','running machine','ramp','computer','notebook','recorder'} 

 
def my(): 
    print myhome.difference(yourhome) 
def you(): 
    print yourhome.difference(myhome) 
def together(): 
    print myhome.intersection(yourhome) 
def All(): 
    print myhome.union(yourhome) 
def count(): 
    d=dict() 
    for c in myhome: 
        if c not in d: 
            d[c]=1 
        else : 
            d[c]=d[c]+1 
    for c in yourhome: 
        if c not in d: 
            d[c]=1 
        else : 
            d[c]=d[c]+1 
    print d 
    print len(d) 

 
 
def lap9(): 
    charCount() 
    word=raw_input("input word:") 
    countDigitsLetter(word) 
    my() 
    you() 
    together() 
    All() 
    count() 
 
def main(): 
    lap9() 
 

 
if __name__=="__main__": 
    main() 
