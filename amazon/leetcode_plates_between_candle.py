"""
There is a long table with a line of plates and candles arranged on top of it. You are given 
a 0-indexed string s consisting of characters '*' and '|' only, where a '*' represents a plate 
and a '|' represents a candle.

You are also given a 0-indexed 2D integer array queries where queries[i] = [lefti, righti] 
denotes the substring s[lefti...righti] (inclusive). For each query, you need to find the number of plates between candles that are in the substring. A plate is considered between candles if there is at least one candle to its left and at least one candle to its right in the substring.

For example, s = "||**||**|*", and a query [3, 8] denotes the substring "*||**|". The number of plates between candles in this substring is 2, as each of the two plates has at least one candle in the substring to its left and right.
Return an integer array answer where answer[i] is the answer to the ith query.
"""

"""
Input: s = "**|**|***|", queries = [[2,5],[5,9]]
Output: [2,3]
Explanation:
- queries[0] has two plates between candles.
- queries[1] has three plates between candles.


Constraints:

3 <= s.length <= 105
s consists of '*' and '|' characters.
1 <= queries.length <= 105
queries[i].length == 2
0 <= lefti <= righti < s.length

"""



"""
approach -- 

initlaize the ptrs at the bounday in 

move both the ptrs till find the plate and if left != right and also right - 1 != "|" and left + 1 != "|" 

the inintalize a ptr inside and count all 

repeat for all budary  

"""
from typing import List

class Solution_slow:
    """
    The slow soluton 
    """
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        results = []  # Store results for each query

        for l, r in queries:
            # Move l to the first '|'
            while l <= r and s[l] != '|':
                l += 1

            # Move r to the last '|'
            while r >= l and s[r] != '|':
                r -= 1  

            # If we found valid candles
            if l < r:
                count = 0  # Plate counter
                for i in range(l + 1, r):
                    if s[i] == '*':
                        count += 1
                results.append(count)
            else:
                results.append(0)

        return results




s = "***|**|*****|**||**|*"


q = [[1,17],[4,5],[14,17],[5,11],[15,16]]


sol = Solution()

print(sol.platesBetweenCandles(s,q))