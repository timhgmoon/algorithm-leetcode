"""
A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros. For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.

Given a string n that represents a positive decimal integer, return the minimum number of positive deci-binary numbers needed so that they sum up to n.
Example:
Input: n = "32"
Output: 3
Explanation: 10 + 11 + 11 = 32
"""

class Solution:
    def minPartitions(self, n: str) -> int:
        n_list = list(n)
        max = 0
        for i in range(len(n_list)):
            if max < int(n_list[i]):
                max = int(n_list[i])
                
        return max
            
