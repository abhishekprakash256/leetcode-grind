"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""

"""
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

"""


"""

max_long = 0

nums.sort()

[1,2,3,4,100,200]

cur_length = 1


for i in range(1,len(nums)):

    if nums[i] - nums[i-1] = 1:

        cur_length += 1 

    else:

        max_long = max(max_long, cur_length)
        cur_length = 1 
    


"""

from typing import List



class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Function to find the length of the longest consecutive sequence.
        paases the leetcode
        """
        # Base case: if nums is empty, return 0
        if not nums:
            return 0
        
        # Sort the numbers
        nums.sort()

        # Initialize the variables
        max_len = 1
        cur_len = 1

        # Loop through sorted list to find longest consecutive sequence
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:  # Skip duplicates
                continue
            elif nums[i] - nums[i - 1] == 1:
                cur_len += 1
            else:
                max_len = max(cur_len, max_len)
                cur_len = 1

        # Final check for the maximum length
        return max(max_len, cur_len)




lst = [0,3,7,2,5,8,4,6,0,1]


sol = Solution()
print(sol.longestConsecutive(lst))









        