print "triangle!"
print "input"

q=raw_input("size:")
q=int(q)

for i in range(q):
    print " "*(q-i)+"*"*(i*2-1)