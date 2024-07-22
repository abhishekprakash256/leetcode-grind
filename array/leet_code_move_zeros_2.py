"""

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]


Input: nums = [0]
Output: [0]
"""



"""
#constraints 

len(nums) == 0 or len(nums) == 1
	return empty or nums 



1.Brute force 

- start the loop see 
- pop and count 
- append as per counter 




"""




class Solution:
	def moveZeroes_bruteforce(self, nums) -> None:
		"""
		The function to modify the zeros in the nums 
		#the code passes in leetcode 
		"""

		#base case 
		if len(nums) == 0 :
			nums = nums

		if len(nums) == 1 :
			nums = nums

		#iter and counter
		count , i = 0 , 0 

		#count the number of zeros 

		while i < len(nums):

			if nums[i] == 0:

				nums.pop(i)
				count += 1 

			else:

				i += 1 


		#add the zeros

		for a in range(0,count):

			nums.append(0)
			

	def moveZeroes(self, nums: List[int]) -> None:
		left = 0

		for right in range(len(nums)):
		    if nums[right] != 0:
		        nums[right], nums[left] = nums[left], nums[right]
		        left += 1

		return nums






















	 