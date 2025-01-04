"""
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.

"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
    	"""
    	passes leetcode

    	"""
        ones, twos = 0, 0
        
        for num in nums:
            # Update 'ones' with the current number, excluding bits in 'twos'
            ones = (ones ^ num) & ~twos
            
            # Update 'twos' with the current number, excluding bits in 'ones'
            twos = (twos ^ num) & ~ones
            
        return ones
