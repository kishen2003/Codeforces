import sys


def solve():
    inputs = sys.stdin.read().split()
    n = int(inputs[0])
    a = list(map(int, inputs[1:]))
    left = right = -1
    for i in range(n - 1):
        if a[i + 1] < a[i]:
            left = i
            break
    if left == -1:
        sys.stdout.write("yes\n1 1")
        return
    for i in range(n - 1, 0, -1):
        if a[i - 1] > a[i]:
            right = i
            break
    a[left : right + 1] = reversed(a[left : right + 1])
    for i in range(n - 1):
        if a[i + 1] < a[i]:
            sys.stdout.write("no")
            return
    sys.stdout.write("yes\n" + str(left + 1) + " " + str(right + 1))


if __name__ == "__main__":
    solve()
