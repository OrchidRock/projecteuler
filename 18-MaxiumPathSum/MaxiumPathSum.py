triangle = [75,
95,64,
17,47,82,
18,35,87,10,
20,4,82,47,65,
19,1,23,75,3,34,
88,2,77,73,7,63,67,
99,65,4,28,6,16,70,92,
41,41,26,56,83,40,80,70,33,
41,48,72,33,47,32,37,16,94,29,
53,71,44,65,25,43,91,52,97,51,14,
70,11,33,28,77,73,17,78,39,68,17,57,
91,71,52,38,17,14,91,43,58,50,27,29,48,
63,66,4,68,89,53,67,30,73,16,69,87,40,31,
4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]

triangleListLen = len(triangle)
rownum = 15
#print(triangleListLen)
cache = [[0 for j in range(0,rownum+1)] for i in range(0,rownum+1)]
step = [[0 for j in range(0,rownum+1)] for i in range(0,rownum+1)]

def maxiumpathsum(i,j,step):
    k = int((i*(i-1))/2) + j
    if k > triangleListLen:
        return 0
    if cache[i][j] > 0:
        return cache[i][j]
    left = maxiumpathsum(i+1,j,step)
    right = maxiumpathsum(i+1,j+1,step)
    if left > right:
        cache[i][j] = left + triangle[k-1] 
        step[i][j] = j
    else:
        cache[i][j] = right + triangle[k-1] 
        step[i][j] = j+1
    return cache[i][j]
def printstep(step,i,j):
    k = int((i*(i-1))/2) + j
    if k >= triangleListLen:
        return
    print(str(triangle[k-1]) + " next = " + str(step[i][j]) )
    printstep(step,i+1,step[i][j])
#printstep(step,1,1)
print(step)
print(maxiumpathsum(1,1,step))
