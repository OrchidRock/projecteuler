#
#
#
#

def load_primes_table(filename):
    primes_table = []
    with open(filename) as f:
        for line in f:
            primes_table.append(int(line))

    return primes_table


def solve(n, pt):
    for f in pt:

        while n % f == 0:
            n = n / f

        if n == 1:
            return f

    print("The primes_table  is too small")


if __name__ == "__main__":
    import sys
    pt = load_primes_table(sys.argv[1])
    res = solve(int(sys.argv[2]), pt)
    print(res)
