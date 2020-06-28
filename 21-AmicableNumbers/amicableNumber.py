import math

Limit = 10000000

table = [0 for i in range(0,Limit)]
skip = [0 for i in range(0,Limit)]

def sumDivisors(n):
    if n < 2:
        return n
    q = (int)(math.sqrt(n))
    s = 0
    for i in range(2,q+1):
        d = n // i
        if n % i == 0 and i < d:
            s += i + d
            #print(str(i) + " " + str(d))
    s += 1
    return s

amicablesum = 0
for i in range(1,Limit):
    if skip[i]:
        continue
    p = 0
    q = 0
    if table[i] > 0:
        p = table[i]
    else:
        p = sumDivisors(i)
        table[i] = p
    if p >= Limit: # 越界
        continue
    if table[p] > 0:
        q = table[p]
    else:
        q = sumDivisors(p)
        table[p] = q
    if q == i and i != p:
        print(str(i) + "---" + str(p))
        skip[p] = 1
        amicablesum += i + p
print(amicablesum)
