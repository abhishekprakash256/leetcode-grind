"""
Given an integer array nums, find a that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Note that the product of an array with a single element is the value of that element.

"""

"""
Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.



"""


"""

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any subarray of nums is guaranteed to fit in a 32-bit integer.



"""


"""
approach --> 


curr_mul = nums[0]
max_mul = nums[0]


for i in range(1 , len(nums)) :

	curr_mul = max(curr_mul , nums[i] * curr_mul)

	max_mul = max(max_mul , curr_mul)



return max_mul

"""

from typing import List

class Solution_W:
	def maxProduct(self, nums: List[int]) -> int:
		"""
		The function to find the max mul array
		"""


		curr_mul = nums[0]
		max_mul = nums[0]


		for i in range(1 , len(nums)) :

			curr_mul = max(nums[i] , nums[i] * curr_mul)

			max_mul = max(max_mul , curr_mul)


		return max_mul





class Solution:
	def maxProduct(self, nums: List[int]) -> int:

		cur_min = nums[0]
		cur_max = nums[0]
		max_val = nums[0]

		for i in range(1, len(nums)):

			prev_max = cur_max
			prev_min = cur_min

			cur_max = max(nums[i], nums[i] * prev_max, nums[i] * prev_min)
			cur_min = min(nums[i], nums[i] * prev_max, nums[i] * prev_min)

			max_val = max(max_val, cur_max)

		return max_val



if __name__ == '__main__':

	nums = [-2,1,-3,4,-1,2,1,-5,4]

	sol = Solution()

	res = sol.maxSubArray(nums)

	print(res)