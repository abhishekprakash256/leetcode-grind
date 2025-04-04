"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
 The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

	Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. 
	The remaining elements of nums are not important as well as the size of nums.
	Return k.

"""


"""
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).


Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

"""


"""
[1,1,2]




"""



class Solution:
	def removeDuplicates(self, nums: List[int]) -> int:
		"""
		The function to removee duplicates in places in a sorted array 
		passes leetcode

		"""

		#base case 
		if len(nums) == 1:
			return 1


		l , r = 0 ,1

		length = len(nums)

		#start the remove loop
		while r < length:

			if nums[l] == nums[r]:
				nums.pop(l)

			else:
				l += 1
				r += 1

			length = len(nums)

		return length


	def removeDuplicates_optimal(self, nums: List[int]) -> int:
		"""
		Leetcode optimal soluton
		"""
		
		l = 1
		for r in range(1,len(nums)):
			if nums[r] != nums[r-1]:
				nums[l] = nums[r]
				l += 1

		return l


