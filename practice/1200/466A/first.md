Problem Link: https://codeforces.com/problemset/problem/466/A

Solution:

Read n, m, a, b

if b / m >= a, then print n*a # buy single ticket everytime if offer is not good
else, find n % m , say rem, print (rem * a) + (n // m ) * b # buy offer tickets, and single for rem

time complexity: o(1)
space complexity: o(1)

verdict:
wrong answer