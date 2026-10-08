import sys


def solve():
    x, y, r = map(int, sys.stdin.readline().strip().split())
    sys.stdout.write(str(x) + " " + str(y + r) + "\n")


if __name__ == "__main__":
    t = int(sys.stdin.readline())
    for _ in range(t):
        solve()
