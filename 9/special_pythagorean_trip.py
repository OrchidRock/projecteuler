#
# c = 1000 - a - b; a^2 + b^2 = c^2; a + b > c
# => 1000/3 < c < 1000/2
# => a + b > 1000/2

from math import floor


def solve():
    s = 1000
    a_limit = floor((s - 3) / 3)
    b_limit = (s - a_limit) / 2

    for a in range(3, a_limit + 1):
        b_limit = floor((s - a) / 2)
        for b in range(a + 1, b_limit + 1):
            c = s - a - b
            if c * c == a * a + b * b:
                print(a, b, c)
                print(a * b * c)


if __name__ == "__main__":
    solve()
