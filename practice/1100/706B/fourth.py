import bisect
import sys


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
            cache_results[coin] = bisect.bisect_right(n, coin)
        outputs.append(str(cache_results[coin]))
    sys.stdout.write("\n".join(outputs))


if __name__ == "__main__":
    solve()
