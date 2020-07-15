from math import sqrt

s = 10000000
s2 = s / 2


def gcd(x, y):
    if x < y:
        tmp = y
        y = x
        x = tmp
    if y == 0:
        return x
    return gcd(y, x % y)  # gcd(x,y) = gcd (y, x mod y)


mlimit = (int)(sqrt(s2)) + 1
for m in range(2, mlimit+1):
    if s2 % m == 0:  # m is s2's factor
        sm = s2 / m
        while sm % 2 == 0:
            sm = sm / 2
        k = 0
        # k must be odd
        if m % 2 == 1:
            k = m + 2
        else:
            k = m + 1

        while k < 2*m and k <= sm:
            if sm % k == 0 and gcd(k, m) == 1:
                d = s2 / (k * m)
                n = k - m
                a = d * (m*m - n * n)
                b = 2 * d * m * n
                c = d * (m*m + n*n)
                print(a, b, c)

            k += 2
