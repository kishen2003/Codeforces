import sys


def binary_search(low, high, coin, n):
    while low <= high:
        mid = (low + high) // 2
        if n[mid] == coin:
            for i in range(mid + 1, high + 1):
                if n[i] > coin:
                    return i
            return high + 1
        elif n[mid] > coin:
            high = mid - 1
        else:
            low = mid + 1
    return high + 1


def solve():
    ln = int(sys.stdin.readline())
    n = list(map(int, sys.stdin.readline().split()))
    n.sort()
    q = int(sys.stdin.readline())
    for _ in range(q):
        coin = int(sys.stdin.readline())
        sys.stdout.write(str(binary_search(0, ln - 1, coin, n)) + "\n")


if __name__ == "__main__":
    solve()
