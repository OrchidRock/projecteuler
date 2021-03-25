#
# The function's program is amazeing, but we don't have
# to object to another way
# Date: 2020.7.9
#
# CLI: python3 -m 1.multiples_of_3_5 <n>
#

# print('__file__={0:<35} | __name__={1:<25} | __package__={2:<25}'.format(__file__, __name__, str(__package__)))

# from lib import common
from lib.common import sum_series

# def sum_series(high, step=1, low=1):
#    n = (high - low)/step + 1
#    s = n * ((high + low) / 2)
#    print(f'sum_series ({high}, {step}, {low}):{s}')
#    return s


def solve(n):
    """TODO: Docstring for solve.
    :returns: TODO

    """
    a3 = n // 3
    a5 = a3 // 5

    s1 = (sum_series(a3) - sum_series(a5) * 5) * 3

    b5 = n // 5
    # b3 = b5 // 3

    s2 = (sum_series(b5)) * 5

    return s1 + s2


# lazy-value
def stream_enumerate_interval(low, high):
    for i in range(low, high):
        yield i


# slove2 much slower than solve1.
def solve2(n):
    s = 0
    for i in stream_enumerate_interval(1, n):
        if (i % 3 == 0) or (i % 5 == 0):
            s += i

    return s


if __name__ == "__main__":
    import sys
    s = solve(int(sys.argv[1]) - 1)
    print("s1:", s)
    s2 = solve2(int(sys.argv[1]) - 1)
    print("s2:", s)
