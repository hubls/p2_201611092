temp=input("user input temperature : ")
sel=raw_input("F or C : ")
print temp, sel
if sel=='F':
    result=(temp-32)/1.8
    print result, "C"
elif(sel=='C'):
    print result,"C"
else:
    print "input Error"