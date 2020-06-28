stream = open("p022_names.txt","r")
nameslist = stream.readline().split("\",\"")
n = len(nameslist)
#print(nameslist[0])
#print(nameslist[n-1])
nameslist[0] = nameslist[0][1:]
nameslist[n-1] = nameslist[n-1][:-1]
#print(nameslist[0])
#print(nameslist[n-1])
nameslist.sort()
result = 0
for index in range(0,n):
    name = nameslist[index]
    sumalphas = 0
    for j in range(0,len(name)):
        sumalphas += (ord(name[j]) - ord('A') + 1)
    result += ((index+1)*sumalphas)
print(result)
