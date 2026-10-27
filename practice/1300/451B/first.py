import sys


def solve():
    inputs = sys.stdin.read().split()
    n = int(inputs[0])
    a = list(map(int, inputs[1:]))
    found_first_unsorted = (False, -1)
    for i in range(1, n):
        if a[i] < a[i - 1]:
            found_first_unsorted = (True, i - 1)
            break
    if not found_first_unsorted[0]:
        sys.stdout.write("yes\n1 1")
        return
    found_second_unsorted = (False, -1)
    for i in range(found_first_unsorted[1] + 1, n):
        if a[i] >= a[found_first_unsorted[1]]:
            found_second_unsorted = (True, i - 1)
            break
    if not found_second_unsorted[0]:
        for i in range(found_first_unsorted[1] + 1, n):
            if a[i - 1] < a[i]:
                sys.stdout.write("no")
                return
        if a[-1] >= a[found_first_unsorted[1] - 1]:
            sys.stdout.write(
                "yes\n" + str(found_first_unsorted[1] + 1) + " " + inputs[0]
            )
        else:
            sys.stdout.write("no")
        return
    for i in range(found_first_unsorted[1] + 1, found_second_unsorted[1] + 1):
        if a[i - 1] < a[i]:
            sys.stdout.write("no")
            return
    for i in range(found_second_unsorted[1] + 2, n):
        if a[i] < a[i - 1]:
            sys.stdout.write("no")
            return
    if (
        a[found_second_unsorted[1]] >= a[found_first_unsorted[1] - 1]
        or found_first_unsorted[1] == 0
    ):
        sys.stdout.write(
            "yes\n"
            + str(found_first_unsorted[1] + 1)
            + " "
            + str(found_second_unsorted[1] + 1)
        )
    else:
        sys.stdout.write("no")


if __name__ == "__main__":
    solve()
