k = 100

nsum = k*(k+1)*0.5

sumsquare = 0
for i in range(1,k+1):
    sumsquare += i*i
print nsum * nsum - sumsquare
