"""
Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.
"""

"""
Example 1:

Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.

Example 2:

Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.

Example 3:

Input: nums = [-3,-2,-3]
Output: -2
Explanation: Subarray [-2] has maximum sum -2.

Constraints:

n == nums.length
1 <= n <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104


"""


"""
approach ---

use the first algo -- 

[1,-2,3,-2]

out = 3

[5,-3,5]

out = 10 

[-3,-2,-3]

out = -2



"""


from typing import List

class Solution:
	def maxSubarraySumCircular(self, nums: List[int]) -> int:
		"""
		Finds the maximum possible sum of a non-empty subarray in a circular array.
		"""
		# Function to calculate the maximum subarray sum using Kadane's algorithm
		def kadane_max(arr: List[int]) -> int:
			max_sum = current_sum = arr[0]
			for num in arr[1:]:
				current_sum = max(num, current_sum + num)
				max_sum = max(max_sum, current_sum)
			return max_sum

		# Function to calculate the minimum subarray sum using Kadane's algorithm
		def kadane_min(arr: List[int]) -> int:
			min_sum = current_sum = arr[0]
			for num in arr[1:]:
				current_sum = min(num, current_sum + num)
				min_sum = min(min_sum, current_sum)
			return min_sum

		# Calculate the total sum of the array
		total_sum = sum(nums)

		# Calculate the maximum subarray sum (normal case)
		max_kadane = kadane_max(nums)

		# Calculate the minimum subarray sum
		min_kadane = kadane_min(nums)

		# Handle the edge case where all elements are negative
		if max_kadane < 0:
			return max_kadane

		# Calculate the maximum subarray sum (circular case)
		max_circular = total_sum - min_kadane

		# Return the maximum of the normal and circular cases
		return max(max_kadane, max_circular)


































