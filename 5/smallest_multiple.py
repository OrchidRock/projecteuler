#
# How can we solve this problem not to use the primes table?
#
from math import log, floor, pow


def is_prime(n, prefix_primes_table):
    res = n

    for prime in prefix_primes_table:
        while res % prime == 0:
            res = res // prime

    return res != 1


def solve(n):
    factor = 2
    res = 1
    prefix_primes_table = []

    while factor <= n:
        if is_prime(factor, prefix_primes_table):
            prefix_primes_table.append(factor)

            expont = floor(log(n)/log(factor))
            res = res * (int)(pow(factor, expont))

        if factor == 2:
            factor += 1
        else:
            factor += 2

    return res


if __name__ == "__main__":
    import sys
    print(solve(int(sys.argv[1])))
