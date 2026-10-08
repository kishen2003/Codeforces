import sys


def solve():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    ans = [False] * n
    previous_ones = []
    for i in range(n):
        if s[i] == "1":
            previous_ones.append(i)
            ans[i] = True
        elif s[i] == "2" and previous_ones:
            ans[i] = True
            ans[previous_ones.pop()] = False
    ans = [str(i) for i, a in enumerate(ans, 1) if a]
    sys.stdout.write(str(len(ans)) + "\n")
    sys.stdout.write(" ".join(ans))
    sys.stdout.write("\n")


if __name__ == "__main__":
    t = int(sys.stdin.readline())
    for _ in range(t):
        solve()
