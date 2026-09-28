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
Memory: 2100 KB
