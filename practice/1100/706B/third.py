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
    inputs = sys.stdin.read().split()
    ln = int(inputs[0])
    n = list(map(int, inputs[1 : ln + 1]))
    n.sort()
    q = int(inputs[ln + 1])
    outputs = []
    cache_results = {}
    for i in range(q):
        coin = int(inputs[i + ln + 2])
        if coin not in cache_results:
            cache_results[coin] = binary_search(0, ln - 1, coin, n)
        outputs.append(str(cache_results[coin]))
    sys.stdout.write("\n".join(outputs))


if __name__ == "__main__":
    solve()
