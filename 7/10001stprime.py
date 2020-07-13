from math import sqrt

primestable = [2,3]
index = 1
maxindex = 200

while index <= maxindex:
    currprime = primestable[index]
    nextprime = currprime
    while True: # find next prime
	nextprime += 2 # prime must be odd
	limit = sqrt(nextprime)
	isprime = True
	for p in primestable:
	    if p > limit: # prime
		break;
	    if nextprime % p == 0: # not prime
		isprime = False
		break;
	if isprime:
	    print nextprime,
            print ",",
	    primestable += [nextprime]
	    index += 1
	    break
print primestable[maxindex]
