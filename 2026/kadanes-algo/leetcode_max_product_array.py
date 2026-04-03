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

		max_so_far = nums[0]
		min_so_far = nums[0]
		result = nums[0]

		for i in range(1, len(nums)):

			# Important: store temp
			temp_max = max(nums[i], nums[i] * max_so_far, nums[i] * min_so_far)
			min_so_far = min(nums[i], nums[i] * max_so_far, nums[i] * min_so_far)

			max_so_far = temp_max

			result = max(result, max_so_far)

		return result