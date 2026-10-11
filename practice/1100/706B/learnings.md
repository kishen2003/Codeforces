minimize input reads and output write calls wherever possible

caching results to avoid repeated calculations

bisect module used along with binary search

i was doing the checking the next elements which i was using for loop that made it not o(logn) binary search but o(n) in worst case. You should check for the right boundary in this case instead of the element