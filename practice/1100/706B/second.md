sort and do binary search

sort the n shop prices using list sort O(nlogn)

instead of checking every shop do binary search and return index which is greater than coin - O(log n)

time complexity: O(nlogn) + O(qlogn)
space complexity: O(n) - shop prices

binary search:(low, high, coin, n)

mid = (low + high) // 2

if n[mid] == coin:
    loop through with i as mid+1 to check next elements are also matching till high
    return i when number is greater than coin
    return high + 1 when loop ends

elif n[mid] > coin:
    binary search (low, mid-1, coin)

else
    binary search (mid+1, high, coin)

return high + 1 for low > high


verdict:
time limit exceeded