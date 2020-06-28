s = 1000
aLimit = ((s-3)/3)
bLimit = (s - aLimit)/2

print aLimit,bLimit

for a in range(3,aLimit+1):
    bLimit = (s-a)/2
    for b in range(a+1,bLimit+1):
        c = s - a -b
        if c*c == (a*a + b*b):
            print (a,b,c)
                

