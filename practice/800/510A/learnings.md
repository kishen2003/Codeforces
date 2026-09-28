* In algorithm, it is mentioned that if n is divisilbe by 4 or if n is odd, but it should be mentioned like for each row i in n, if i is divisible by 4, or if i is odd.
* There are two things: auxiliary space and space complexity.
  * auxiliary space - temporary space used by algorithm, excluding input and output.
  * space complexity - includes both i/o space and auxiliary space. (total space)
* Here the space complexity is not O(1), it is O(m) because python creates a temporary string when doing "." * (m-1), but it can theoretically be optimized to O(1), by looping and printing one by one, but it is unnecessary and slow for this problem.
