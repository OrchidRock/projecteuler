#n = 600851475143
#n= 444444444444444
n = 100897982

factor =2 
lastFactor = 1
loopcount = 0
while n > 1:
    loopcount += 1
    if n % factor == 0:
	lastFactor = factor
	n = n / factor
	while n % factor == 0:
	    loopcount += 1
	    n = n / factor
    factor += 1
print "loopcount:",loopcount
print lastFactor




    
