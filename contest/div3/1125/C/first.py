import sys


def solve():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    ans = 0
    odd_sums = [a[i] + a[i + 2] - a[i + 4] for i in range(0, n - 4, 2)]
    even_sums = [a[i] + a[i + 2] - a[i + 4] for i in range(1, n - 4, 2)]
    for i in range(len(odd_sums)):
        for j in range(len(even_sums)):
            if odd_sums[i] == even_sums[j]:
                ans += 1
        for j in range(i + 3, len(odd_sums)):
            if odd_sums[i] == odd_sums[j]:
                ans += 1
    for i in range(len(even_sums)):
        for j in range(i + 3, len(even_sums)):
            if even_sums[i] == even_sums[j]:
                ans += 1
    sys.stdout.write(str(ans) + "\n")


if __name__ == "__main__":
    t = int(sys.stdin.readline())
    for _ in range(t):
        solve()
