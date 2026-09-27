import sys


def solve():
    a, b, c = map(int, sys.stdin.readline().strip().split())
    if a + b == c or a + c == b or b + c == a:
        sys.stdout.write("YES\n")
    else:
        sys.stdout.write("NO\n")


if __name__ == "__main__":
    t = int(sys.stdin.readline())
    for _ in range(t):
        solve()
