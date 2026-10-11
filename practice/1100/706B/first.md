Problem Link: https://codeforces.com/problemset/problem/706/B

Solution:
Read n shop prices
Read number of days q

for each day:
read coin for that day
set total to zero
iterate through the list of shop prices and find total number of shops with prices less than or equal to coin on that day
print the total

Complexity:
Time: O(qn)
Space: O(n)

Verdict:
Time Limit Exceeded
