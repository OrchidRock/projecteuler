limit = 4000000
sum = 0
a = 1
b = 1
addcount = 0
c = a + b
while b < limit:
    if b % 2 == 0:
	sum += b
    addcount += 1
    tmp = a+b
    a = b
    b = tmp
    #sum += c
    #a = b + c
    #b = c + a
    #c = a + b
    #addcount += 1
print "sum:",sum
print "addcount:",addcount
	
