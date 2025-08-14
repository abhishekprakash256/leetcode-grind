"""
Given an integer array nums and an integer k, modify the array in the following way:

	choose an index i and replace nums[i] with -nums[i].

You should apply this process exactly k times. You may choose the same index i multiple times.

Return the largest possible sum of the array after modifying it in this way.

"""


"""

Example 1:

Input: nums = [4,2,3], k = 1
Output: 5
Explanation: Choose index 1 and nums becomes [4,-2,3].

Example 2:

Input: nums = [3,-1,0,2], k = 3
Output: 6
Explanation: Choose indices (1, 2, 2) and nums becomes [3,1,0,2].

Example 3:

Input: nums = [2,-3,-1,5,-4], k = 2
Output: 13
Explanation: Choose indices (1, 4) and nums becomes [2,3,-1,5,4].



"""


"""

approach -- 

find the min value with each pass and make them positive 

just them postive k times and do the sum 


loop over and make positive by making -ve postive 


what if I sort 

sort and replace from start with -ve values 


"""

from typing import List


class Solution:
	def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
		"""
		The function find the max sum of the array 
		"""
		if k < 1 :

			return sum(nums)


		#sort the array 
		nums.sort()

		#iter to change the -ve values
		i = 0

		while i < len(nums) and k > 0 and nums[i] < 0 :

			nums[i] = -nums[i]

			i += 1 
			k -= 1 

		if k % 2 == 1 :

			nums.sort()

			nums[0] = -nums[0]

		return sum(nums) 






if __name__ == "__main__" :


	sol = Solution()

	nums = [3,-1,0,2]

	print(sol.largestSumAfterKNegations(nums , 3))





