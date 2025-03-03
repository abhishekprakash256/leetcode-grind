"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""


"""

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.

"""


"""

approach -- 

using a dfs aproach 

add a empty list in last

not have repetative 

[1,2,3]

[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]


the dfs condn and base case 

exhaust the list 






"""











"""
dry run 

[1,2,3]

[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]

"""


class Solution:
    """
    passes the leetcode
    """

    def __init__(self):
        self.result = []

    def helper_dfs(self, idx, temp_lst):
        """
        Helper function to find all possible subsets using DFS.
        """

        # Append the current subset to the result list
        self.result.append(temp_lst[:])

        for i in range(idx, len(self.nums)):
            # Recursively call DFS with the next index and updated subset
            self.helper_dfs(i + 1, temp_lst + [self.nums[i]])

    def subsets(self, nums):
        """
        The function to find all possible subsets of the array.
        """

        self.nums = nums
        self.result = []  # Reset result for each function call
        self.helper_dfs(0, [])
        return self.result





sol = Solution()

nums = [1,2,3]

print(sol.subsets(nums))
