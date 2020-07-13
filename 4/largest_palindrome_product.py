#
# 11        = 0 (mod 11)
# 101       = 0 (mod 11)
# 1001      = 0 (mod 11)
# 10001     = 0 (mod 11)
# 100001    = 0 (mod 11)
# 1000001   = 0 (mod 11)
# 10000001  = 0 (mod 11)
#  ...


def reverse(num):
    reversed = 0

    while num > 0:
        reversed = 10 * reversed + num % 10
        num = num // 10

    return reversed


def is_palindrome(n):
    return n == reverse(n)


def solve():
    a = 999
    largest_palindrome = 0

    while a >= 100:
        if a % 11 == 0:
            b = 999
            db = 1
        else:
            b = 990
            db = 11

        while b >= a:
            if a * b <= largest_palindrome:
                break

            if is_palindrome(a*b):
                largest_palindrome = a * b

            b = b - db

        a = a - 1

    return largest_palindrome


if __name__ == "__main__":
    print(solve())
