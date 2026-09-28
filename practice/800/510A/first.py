import sys


def solve():
    n, m = map(int, sys.stdin.readline().split())
    for i in range(1, n + 1):
        if i % 2 == 1:
            sys.stdout.write("#" * m + "\n")
        elif i % 4 == 0:
            sys.stdout.write("#" + "." * (m - 1) + "\n")
        else:
            sys.stdout.write("." * (m - 1) + "#\n")


if __name__ == "__main__":
    solve()
