"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""

"""

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104

"""


"""
approach -- 

i , j = 0 , len(nums) - 1 

use binary search 

"""


class Solution():

	def searchInsert(self, nums: List[int], target: int) -> int:
		"""
		The function to find the search place or the insert place of the target
		"""

		#constraints
		if len(nums) == 1:

			if nums[0] == target :

				return 0 

			elif nums[0] < target:

				return 1

			else :

				return 0 


		#initialize the ptrs 
		i , j = 0 , len(nums) 

		#start the search loop 
		while i <= j :

			mid = (i+j) // 2 

			if nums[mid] == target :

				return mid

			elif nums[mid] < target :

				i = mid + 1 

			else:

				j = mid - 1 


		return i










































