
#
# (1 + 2 + 3 + ...)^2 = ((n * (n + 1)) / 2)^2
#
# 1^2 + 2^2 + 3^2 = (n * (n + 1) (2 * n + 1)) / 6


def solve(n):

    res = (3 * (n ** 4) + 2 * (n ** 3) - 3 * (n ** 2) - 2 * n) / 12

    return res


if __name__ == "__main__":
    import sys
    print(solve(int(sys.argv[1])))
