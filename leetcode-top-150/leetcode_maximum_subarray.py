"""
Given an integer array nums, find the 
subarray
with the largest sum, and return its sum.
"""

"""
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

[-1,-3]

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104

"""


"""
approach -- 

max sum a -inf 

constarints 
if len(nums) == 1:
	return nums[0]


two pointer ? but adjacent ? 

when value is -ve leave the value and move 

when value is +ve move to next

sliding window

so start with 0 and 1st index 

then get the max value 

if the value gets negative 

move right + 1 
and left to right 



"""

class Solution():

	def maxSubArray(self, nums: List[int]) -> int:
		"""
		The function to find the max sub array
		"""
		
		#constraints 
		if len(nums) == 1:
			return sum(nums)

		#make the temp sum 
		max_sum = 0 

		for i in range(1,len(nums)) :

			









		