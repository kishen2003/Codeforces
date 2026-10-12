import sys


def solve():
    n, m, a, b = map(int, sys.stdin.readline().split())
    if b / m >= a:
        sys.stdout.write(str(n * a))
    else:
        sys.stdout.write(str(n % m * a + n // m * b))


if __name__ == "__main__":
    solve()
