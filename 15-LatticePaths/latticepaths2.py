n = 20
p = [[0 for j in range(0,n+1)] for i in range(0,n+1)]
def counterrouters(n,m):
    #print(str(n)+" " +str(m))
    if n == 0 or m == 0:
        return 1
    if p[n][m] > 0:
        return p[n][m]
    else:
        p[n][m-1] = counterrouters(n,m-1)
        p[n-1][m] = counterrouters(n-1,m)
        return p[n][m-1]+p[n-1][m]
print(counterrouters(n,n))
