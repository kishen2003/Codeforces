I don't know if i can improve the time complexity

Now i can see two improvements:
i/o handling
caching

for i/o:
read all inputs at once and print all output at once


for caching:
store previous q values in a dict and try to do cache hits


time complexity: O(nlogn) + O(qlogn)
spcae complexity: O(n) + O(q)

verdict:
accepted