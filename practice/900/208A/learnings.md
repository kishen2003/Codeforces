Time complexity is O(n^2)
because of 
x in list       → O(n)
list.remove(x)  → O(n)

it can be O(n)

if you use list comprehension [x for x in list if x]

also split(delimiter) leaves empty strings in the list when they appear at the begining/end/consecutively