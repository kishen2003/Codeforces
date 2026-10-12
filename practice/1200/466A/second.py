import sys


def solve():
    n, m, a, b = map(int, sys.stdin.readline().split())
    if b / m >= a:
        sys.stdout.write(str(n * a))
    else:
        rem = min(n % m * a, b)
        sys.stdout.write(str(rem + n // m * b))


if __name__ == "__main__":
    solve()
