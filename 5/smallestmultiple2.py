from math import sqrt,log,floor,pow
k = 50

primestable = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

N = 1
limit = sqrt(k)
index = 0
while primestable[index] <= k:
    expont = 1
    primefactor = primestable[index]
    if primefactor <= limit:
	expont = floor(log(k)/log(primefactor))
    N = N * (int)(pow(primefactor,expont))
    index += 1
print N
