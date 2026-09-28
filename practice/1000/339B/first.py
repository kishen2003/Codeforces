import sys


def solve():
    n, _ = map(int, sys.stdin.readline().split())
    m = list(map(int, sys.stdin.readline().split()))
    current_house = 1
    time_taken = 0
    for t in m:
        if t > current_house:
            time_taken += t - current_house
        elif t < current_house:
            time_taken += n - current_house + t
        current_house = t
    sys.stdout.write(str(time_taken))


if __name__ == "__main__":
    solve()
