import sys


def solve():
    _ = sys.stdin.readline()
    n = list(map(int, sys.stdin.readline().split()))
    q = int(sys.stdin.readline())
    for _ in range(q):
        c = int(sys.stdin.readline())
        total = 0
        for i in n:
            if i <= c:
                total += 1
        sys.stdout.write(str(total) + "\n")


if __name__ == "__main__":
    solve()
