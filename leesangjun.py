temp=input("user input temperature : ")
sel=raw_input("F or C : ")
print temp, sel
if sel=='F':
    result=(temp-32)/1.8
    print result, "C"
elif sel=='C':
    result=(temp*1.8+32)
    print result,"F"
else:
    print "input Error"
