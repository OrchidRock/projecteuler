Limit = 1000000

maxstep = 0
maxstepindex = 0


for i in range(1,Limit):
    num = i
    step = 0
    while num != 1:
        if num % 2 ==0:
            num /= 2
        else:
            num = num * 3 + 1
        step += 1

    if step > maxstep:
        maxstep = step
        maxstepindex = i
        
print (maxstepindex,maxstep)
