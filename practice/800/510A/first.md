Problem Link: [codeforces.com/problemset/problem/510/A](https://codeforces.com/problemset/problem/510/A)

## Solution:

* Read the inputs: n (rows) and m (columns)
* print n rows:
* for each row if n is odd print m times "#"
* else if n is divisible by 4 print one time "#" and (m - 1) times "."
* else print (m - 1) times "." and one time "#"

### Complexity:

Time: O(nm) - Loop through n rows and each row print m chars
Space: O(1) - Three integer variables (n, m, i)

### Result:

Verdict: Accepted
Time: 78 ms
Memory: 0 KB
