l =["one","two","three","four","five","six","seven",
    "eight","nine","ten","eleven","twelve","thirteen",
    "fourteen","fifteen","sixteen","seventeen","eighteen",
    "nineteen"]
l2 = ["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
hundred = len("hundred")
thousand = len("thousand")
andlen = len("and") 

n = 1000
p = [0 for i in range(0,n+1)]

def countNumberLetter(n):
    if n == 0:
        return 0
    if p[n] > 0:
        return p[n]
    sumtmp = 0

    if n < 20:
        sumtmp = len(l[n-1])
        #else:
            #nstr = str(n % 10000)
            #nlist = [0 for i in range(0,4-len(nstr))] 
            #nlist.extend([int(key) for key in list(nstr)])
    elif n < 100:
        digit = n // 10
        carry = n % 10
        sumtmp += len(l2[digit-2])
        if carry > 0:
            sumtmp += len(l[carry-1])
        else:
            pass
    elif n >= 100 and n < 1000:
        digit = n // 100
        carry = n % 100
        sumtmp += len(l[digit-1]) + hundred
        if carry > 0:
            sumtmp += andlen 
            sumtmp += countNumberLetter(carry) 
            sumtmp -= countNumberLetter(carry-1)
        else:
            pass
    elif n >= 1000 and n < 10000:
        digit = n // 1000
        carry = n % 1000
        sumtmp += len(l[digit-1]) + thousand
        if carry > 0:
            sumtmp += andlen
            sumtmp += countNumberLetter(carry) 
            sumtmp -= countNumberLetter(carry-1)
        else:
            pass
    p[n] = countNumberLetter(n-1) + sumtmp
    return p[n]

countNumberLetter(n)
print(p[n])
print(p[99])
#print(countNumberLetter(342))
#print(countNumberLetter(115))
