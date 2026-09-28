Problem Link: https://codeforces.com/problemset/problem/339/B

Solution:

Read n houses and m tasks
Read a list of m tasks
current house is 1
time taken is 0
Now loop through the list of tasks:
if task is bigger than current house: time taken += task - current house
if task is equal to current house: skip
if task is lesser than current house: time taken += n - current house + task
change current house to t for all cases and then continue the loop

Complexity:
Time: O(n) number of tasks
Space: O(n) list of tasks

Verdict:
Accepted