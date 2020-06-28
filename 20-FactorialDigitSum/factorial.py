import math
n = 69

def factorialToDigit(n):
    sumcount = 0
    for i in range(1,n+1):
        sumcount += math.log(i,10)
    return sumcount
print(factorialToDigit(69))
print(factorialToDigit(70))
