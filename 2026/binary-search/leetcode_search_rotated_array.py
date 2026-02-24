"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) 
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
"""

"""

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:

Input: nums = [1], target = 0
Output: -1



"""


"""

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104

"""



"""

approach -- 

find the pivot is the main point --> 
so three pointers , left , mid and right 

rules 

if left <= mid <= right 

use the simple binary search in the bound to find the target

[1,2,3,4,6,0,-1,-3]

how to find the bounddary to search the point ? --> 

if not left < mid -> pivot here 

if not mid < right -> poivot here 

when found the pivot start search on that end 


[1,2,3,4,5,0]



"""

from typing import List


class Solution:

	def binary_search(self, l : int , r : int , nums: List[int], target: int ) :
		"""
		The simple binary search 
		"""

		while l <= r :

			m = (l + r) // 2

			if nums[m] == target :
				
				return m


			if nums[m] < target :

				l = m + 1

			else :

				r = m - 1 

		return -1



	def search(self, nums: List[int], target: int) -> int:
		"""
		The function to find the target in the rotated array
		"""

		#ptrs 
		l = 0 
		r = len(nums) - 1

		#check if the array if not rotated
		m = (l + r) // 2

		if nums[l] <= nums[m] <= nums[r] :

			return self.binary_search(l , r , nums , target)


		#find the pivot case
		while l <= r :

			m = (l + r) // 2

			if nums[l] > nums[m] :

				#pivot here
				r = m - 1 

			if nums[m] > nums[r] :

				#pivot here
				l = m + 1


			if nums[l] <= nums[m] <= nums[r] :

				return self.binary_search(l , r , nums , target)







if __name__ == '__main__':


	nums = [4,5,6,7,0,1,2]
	target = 0	

	sol = Solution()

	res = sol.search(nums , target)

	print(res)
