
def even_filter(x):
    return x % 2 == 0


def fibs_stream(limit):
    a = 0
    b = 1
    while a <= limit:
        yield a
        c = b
        b = a + b
        a = c


def solve(limit):
    s = 0

    for i in fibs_stream(limit):
        if even_filter(i):
            s += i

    return s


def solve2(limit):
    s = 0
    a = 1
    b = 1
    c = a + b

    while c < limit:
        s += c
        a = b + c
        b = c + a
        c = a + b
    
    return s
    

if __name__ == "__main__":
    import sys
    s = solve(int(sys.argv[1]))
    s2 = solve2(int(sys.argv[1]))
    print(s)
    print(s2)
