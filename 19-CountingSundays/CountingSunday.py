'''
-1900 1901 1902 1903 
 7----6----5----4
-1904*1905 1906 1907
 3----1----7----6
-1908*1909 1910 1911
 5----3----2----1
-1912*1913 1914 1915
 7----5----4----3
-1916*1917 1918 1919
 2----7----6----5
-1920*1921 1922 1923
 4----2----1----7
 
 使用转轮法计算1月份星期天的个数
'''

s = [0,5,5,5,4,4,4,4]
sunday = [7,6,5,4,3,2,1]
sundayIndex = 0 # 7 Jan 1900 is sunday
year = 1900
count = 0
while year <= 1999:
    nextSundayIndex = (sundayIndex + 1) % 7
    if year % 100 != 0:
        if year % 4 == 0: # leap year
            nextSundayIndex = (sundayIndex + 2) % 7
    else:
        if year % 400 == 0: # leap year 
            nextSundayIndex = (sundayIndex + 2) % 7
    count += s[sunday[sundayIndex]]
    print("year = "+str(year)+" startsunday="+str(sunday[sundayIndex]) +
          " sundays="+str(s[sunday[sundayIndex]]) + " count="+str(count))
    sundayIndex = nextSundayIndex
    year += 1
print(count)
