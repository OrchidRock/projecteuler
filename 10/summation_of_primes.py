#
# The sieve method of Eratosthenes.
# BAD!!!


# from lib.common import sum_series
from math import sqrt

LIMIT = 2000000


def solve(n):
    sieve = [False]*n
    n_root_tail = int(sqrt(n))

    sieve[0] = True
    sieve[1] = True

    # mark even number > 2
    for i in range(4, n, 2):
        sieve[i] = True

    for i in range(3, n_root_tail+1, 2):
        if not sieve[i]:  # prime
            for j in range(i*i, n, 2*i):
                sieve[j] = True

    sieved_sum = 0
    for i in range(2, n):
        if not sieve[i]:
            # print(i)
            sieved_sum += i

# Optimising the sieve
# If we get rid of the even numbers, we save (limit-2)/2 crossing out and
# more importantly, we use only half the memory. That allows
# sieving larger ranges and reduces cache misses, thus improving performance.

    return sieved_sum


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        res = solve(int(sys.argv[1]))
    else:
        res = solve(LIMIT)

    print(res)
