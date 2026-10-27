Problem Link: https://codeforces.com/problemset/problem/451/B

Solution:

Read n - size of array 
Read the array

Find the first element which is not sorted, if we can't find then print yes \n 1 1
take the number before it, find the next number which is greater than or equal to that number, if we can't find print yes \n position of number before it and last number
if we can find, then print yes \n position of number before it and position of found number -1, unless you can find a number not sorted after the position of found number then print no

time complexity: O(n) -> traversing the array
space complexity: O(n) -> storing input

verdict:
accepted