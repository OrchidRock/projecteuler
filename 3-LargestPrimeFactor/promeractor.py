from math import sqrt
# 非常烂的算法

loopcount = 0
#Limit = 600851475143
Limit = 100897982
result = 2

def is_prime(n):
    count = 0
    if n == 1:
	return (False,count)
    for i in range(2,int(sqrt(n))+1):
	count = count + 1
	if n % i == 0:
	    return (False,count)
    return (True,count)


for j in range(2,Limit):
    q = j
    loopcount += 1
    if Limit % q == 0:
        print q
	p = Limit / q
	res,count = is_prime(q)
	loopcount += count
	if res:
	    result = q
	    #break
print "loopcount:",loopcount
print result
