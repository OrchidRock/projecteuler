'''
自底向上法
2018.8.17
'''
n = 20
def counterrouters(n,m):
    p = [[1 for j in range(0,m+1)] for i in range(0,n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            p[i][j] = p[i-1][j] + p[i][j-1]
    return p[n][m]
    
print(counterrouters(n,n))
