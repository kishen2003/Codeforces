import sys


def solve():
    s = sys.stdin.readline().strip().split("WUB")
    s = [x for x in s if x]
    sys.stdout.write(" ".join(s))


if __name__ == "__main__":
    solve()
