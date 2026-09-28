import sys


def solve():
    n, _ = map(int, sys.stdin.readline().split())
    m = map(int, sys.stdin.readline().split())
    current_house = 1
    time_taken = 0
    for t in m:
        time_taken += (t - current_house) % n
        current_house = t
    sys.stdout.write(str(time_taken))


if __name__ == "__main__":
    solve()
