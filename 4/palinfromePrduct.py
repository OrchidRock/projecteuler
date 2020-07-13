maxproduct = 0
loopcount = 0
for i in range(100,1000):
    for j in range(100,1000):
	loopcount += 1
	product = i*j
	one = product % 10
	product /= 10
	ten = product % 10
	product /= 10
	hundred = product % 10
	product /= 10
	if product < 100:
	    thousand = product % 10
	    product /= 10
	    tenthousand = product % 10
	    if tenthousand == one and thousand == ten:
		maxproduct = max(i*j,maxproduct)
	else:
	    thousand = product % 10
	    product /= 10
	    tenthousand = product % 10
	    product /= 10
	    hundredthousand  = product % 10
	    if hundredthousand == one and tenthousand == ten and thousand == hundred:
#if (i*j) % 11 == 0:
#		    print i*j,"ok"
#		else:
#		    print i*j,"failed"
		maxproduct = max(i*j,maxproduct)
print "loopcount:",loopcount
print maxproduct
