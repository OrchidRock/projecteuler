#n = 600851475143
#n= 444444444444444
n=100897982

loopcount = 0

if n % 2 == 0:
    n /= 2
    lastFactor = 2
    loopcount += 1
    while n % 2 == 0:
	n /= 2
else:
    lastFactor = 1
factor = 3
while n > 1:
    loopcount += 1
    if n % factor == 0:
	lastFactor = factor
	n = n / factor
	while n % factor == 0:
	    loopcount += 1
	    n = n / factor
    factor += 2
print "loopcount:",loopcount
print lastFactor




    
