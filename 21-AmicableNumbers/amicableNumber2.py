'''
  d(a) > a ?
 这里还可以提升效率：1. 奇数没有偶数因子
                     2. 利用素数
 参考 https://mathschallenge.net/index.php?section=faq&ref=number/sum_of_divisors
'''
import math

# 素数表太小
primestable = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
Limit = 10000000

table = [0 for i in range(0,Limit)]
skip = [0 for i in range(0,Limit)]


def sumDivisors(n):
    if n < 2:
        return n
    primefactorIndex = 0
    result = 1
    tmp = n
    while tmp != 1 and primefactorIndex < len(primestable):
        power = 0
        primefactor = primestable[primefactorIndex]
        while tmp % primefactor == 0:
            power +=1
            tmp //= primefactor
        #print(primefactor,end=' ')
        #print(power)
        primefactorIndex += 1
        result *= (((primefactor**(power+1)) - 1)/(primefactor-1))
    return int(result-n)  

amicablesum = 0
#print(sumDivisors(220))
#print(sumDivisors(284))

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
