"""
Given an array nums of integers and integer k, return the maximum sum such that there exists i < j 
with nums[i] + nums[j] = sum and sum < k. If no i, j exist satisfying this equation, return -1.
"""

"""

Input: nums = [34,23,1,24,75,33,54,8], k = 60
Output: 58
Explanation: We can use 34 and 24 to sum 58 which is less than 60.

Example 2:

Input: nums = [10,20,30], k = 15
Output: -1
Explanation: In this case it is not possible to get a pair sum less that 15.

"""



"""
approach --

sort and use binary search 





"""


nums = [34,23,1,24,75,33,54,8]

class Solution:
	def twoSumLessThanK(self, nums, k: int) -> int:
		"""
		The function to find the sum out equal or less
		"""

		#base case 
		if len(nums) == 1 :

			if nums[0] <= k:

				return nums[0]

			else:

				return -1


		#sort the array
		nums.sort()

		print(nums)

		#initilalize the vars
		i = 0 
		j = len(nums) -  1

		while i < j :

			if nums[i] + nums[j] > k :

				j -= 1 

			else :

				while nums[i] + nums[j] < k :

					i += 1

				return nums[i] + nums[j]

		return -1







	






			
 









if __name__ == "__main__" :

	sol = Solution()

	print(sol.twoSumLessThanK(nums,60))

