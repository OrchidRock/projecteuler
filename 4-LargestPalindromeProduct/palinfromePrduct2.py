maxproduct = 0
loopcount = 0
for i in range(900,1000):
    for j in range(i,1000):
	if i % 11 != 0 and j % 11 != 0:
	    continue
	loopcount += 1
	product = i*j
	one = product % 10
	product /= 10
	ten = product % 10
	product /= 10
	hundred = product % 10
	product /= 10
	
	thousand = product % 10
	product /= 10
	tenthousand = product % 10
	product /= 10
	hundredthousand  = product % 10
	if hundredthousand == one and tenthousand == ten and thousand == hundred:
	    if (i*j) % 11 == 0:
		print i*j,"ok"
	    else:
		print i*j,"failed"
	    maxproduct = max(i*j,maxproduct)
print "loopcount:",loopcount
print maxproduct
