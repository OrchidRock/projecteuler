power = 10000

def sumPowerDigit(n):
    if n == 1:
        return 1
    r = [1]
    l = 1
    for i in range(1,n+1):
        index = 0
        inc = 0
        while index < l:
            k = (r[index]) * 2 + inc
            inc = k // 10
            r[index] = k % 10
            index += 1
        if inc != 0:
            r.append(inc)
            l += 1
        #print(r)
        #print("i = "+str(i))
    return r
#s = [int(key) for key in sumPowerDigit(power)]
#print(s)
print(sum(sumPowerDigit(power)))

