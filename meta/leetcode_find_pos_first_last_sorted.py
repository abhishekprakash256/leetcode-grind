"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending
 position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
"""


"""
Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109


"""

"""

approach -- 

using a normal binary 

search get the first and last point 

then run the custom binary search 

with edge case handling 

"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
    	"""
		The search to find first and last of the occurance
    	"""

    	#constrinats case 
    	
    	#if no nums
    	if not nums :

    		return [-1,-1]

    	#if len of nums == 1
    	if len(nums) == 1:

    		return [0,0]

    	#vars 
    	result = [] 

    	#ptrs 
    	l , r = 0 , len(nums) - 1 
    	idx_target = 0 
    	first , last = 0 ,0 


    	#start the search
    	while l <= r :

    		mid = (l + r) // 2 

    		if nums[mid] == target :

    			idx_target = l

    		elif nums[mid] < target :

    			l = mid + 1 

    		else :

    			r = mid - 1

    	#edge case of first 
    	if idx_target == 0:

    		first = idx_target

    	#edge case of last
    	if idx_target == len(nums) - 1 :

    		last = idx_target

    	













