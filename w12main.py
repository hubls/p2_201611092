﻿def writePythonTextFile(): 
    myfile=open('python.txt', 'w') 
    line1='Python is a widely used high-level, general-purpose, interpreted,\n' 
    myfile.write(line1) 
    line2='dynamic programming language.[23][24]\n' 
    myfile.write(line2) 
    line3='Its design philosophy emphasizes code readability, and\n' 
    myfile.write(line3) 
    line4='its syntax allows programmers to express concepts in fewer lines of code\n' 
    myfile.write(line4) 
    line5='than would be possible in languages such as C++ or Java.[25][26]\n' 
    myfile.write(line5) 
    line6='The language provides constructs intended to enable clear programs on\n' 
    myfile.write(line6) 
    line7='both a small and large scale.[27]\n' 
    myfile.write(line7) 
    myfile.close() 
     
def changeToCap(file): 
    import os 
    mydir=os.getcwd() 
    filename=file 
    myfilename=os.path.join(mydir, filename) 
    try: 
        myfile=open(myfilename, 'r') 
        contents=myfile.readlines() 
        myfile.close() 
        myfile=open(myfilename, 'w') 
        for i in range(0,len(contents)): 
            line=contents[i].upper() 
            myfile.write(line) 
        myfile.close() 
        myfile=open(myfilename, 'r') 
        contents=myfile.read() 
        myfile.close() 
        print contents 
         
         
    except IOError as e: 
        print e 
     
def findWord(file, word): 
    import os 
    mydir=os.getcwd() 
    filename=file 
    myfilename=os.path.join(mydir, filename) 
    try: 
        myfile=open(myfilename, 'r') 
        contents=myfile.readlines() 
        myfile.close() 
        for i in contents: 
            if i.find(word) >= 0: 
                print "Find " + word + " :" + i 
    except IOError as e: 
        print e 

 
def lab12(): 
    import os 
     
    writePythonTextFile() 
     
    
    print "\tUse readline():\n" 
    mydir=os.getcwd() 
    filename='Python.txt' 
    myfilename=os.path.join(mydir, filename) 
    myfile=open(myfilename, 'r') 
    for line in range(0,7): 
        line=myfile.readline() 
        print line 
    myfile.close() 
     
    
    print "\tUse read():\n" 
    myfile=open(myfilename, 'r') 
    contents=myfile.read() 
    myfile.close() 
    print contents 
     
    # 전체 읽기인데 자료구조 list이용 
    print "\tUse readlines():\n" 
    myfile=open(myfilename, 'r') 
    contents=myfile.readlines() 
    myfile.close() 
    print contents 
     
    print "\n" 
     
    file='Python.txt' 
    word="Python" 
    findWord(file, word) 
     
 
    print "Change to Capital:\n" 
    file='Python.txt' 
    changeToCap(file) 
 
def main(): 
    lab12() 
     
if __name__=="__main__": 
    main() 
