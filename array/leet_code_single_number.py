"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""

#test cases 

arr = [2,2,1]
out = 1

arr2 = [1]
out2 = 1


arr3 = [2,2,2,3]
out3 = 3



class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        