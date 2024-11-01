"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the 
array such that nums[i] == nums[j] and abs(i - j) <= k.
"""

"""
Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

"""


from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        Check if there are two indices i and j such that nums[i] == nums[j] and
        abs(i - j) <= k.
        """

        # Base case: If the list has less than 2 elements, return False
        if len(nums) < 2:
            return False

        # Create a hash map to store the index of each number
        mapper = {}

        # Loop over the list
        for i in range(len(nums)):
            if nums[i] in mapper:
                # Check if the absolute difference of indices is less than or equal to k
                if abs(mapper[nums[i]] - i) <= k:
                    return True
            
            # Update the index of the current number
            mapper[nums[i]] = i
        
        return False








