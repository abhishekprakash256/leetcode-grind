"""
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.

Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.
"""


"""
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.

Example 2:

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.

Example 3:

Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.


Constraints:

2 <= k <= 9
1 <= n <= 60


"""

"""
approach -- 

using a list 

append the number to make the sum and check the list length and then equal append the number 

dfs function have list and idx carried



"""

from typing import List



class Solution():
    """
    passes leetcode 
    """

    def __init__(self):

        self.results = []

    def _helper_dfs(self,idx,sum_lst, curr_sum):
        """
        The function to make dfs call for helper function
        """

        #base case 
        if len(sum_lst) == self.k :

            if curr_sum == self.n :

                self.results.append(sum_lst[:])

            return
        
        if curr_sum > self.n :

            return

        #make the recursive calls
        for i in range(idx, 10) :

            sum_lst.append(i)

            self._helper_dfs(i + 1, sum_lst , curr_sum + i)

            #pop the used element
            sum_lst.pop()
        

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        """
        The function to make the combinatiosn that have target sum
        """

        self.n = n 
        self.k = k

        #vars 
        sum_lst = []
        idx = 1
        curr_sum = 0 

        #make the helper call
        self._helper_dfs(idx, sum_lst , curr_sum)

        return self.results




sol = Solution()

res = sol.combinationSum3(k=3,n=9)

print(res)