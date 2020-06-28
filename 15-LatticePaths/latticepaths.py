import math
n = 20

def countRoutes(n):
    result = 1
    for i in range(1,n+1):
        result = result * (n+i)/i
    return result
print(countRoutes(n))
