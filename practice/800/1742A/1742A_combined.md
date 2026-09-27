# Problem: 1742A


## File: first.md

```markdown
Problem Link: [codeforces.com/problemset/problem/1742/A](https://codeforces.com/problemset/problem/1742/A)

## Solution:

### Algorithm:

Read the number of test cases and for each test case do the following:

* Read the three numbers (a,b,c)
* Check all 3 combinations  ((a+b=c), (a+c=b) and (b+c=a))
* If any one of these is true, print "YES" else print "NO"

### Complexity Analysis:

Time: O(1)  - Reading inputs, 3 comparisons (worst case), printing outputs

Space: O(1) - Three integer variables

### Result:

Verdict: Accepted
Time: 62 ms
Space: 2100 KB

```


## File: first.py

```python
import sys


def solve():
    a, b, c = map(int, sys.stdin.readline().strip().split())
    if a + b == c or a + c == b or b + c == a:
        sys.stdout.write("YES\n")
    else:
        sys.stdout.write("NO\n")


if __name__ == "__main__":
    t = int(sys.stdin.readline())
    for _ in range(t):
        solve()

```

