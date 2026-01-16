"""
You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).
"""

"""


Example 1:

Input: nums = [4,2,4,5,6]
Output: 17
Explanation: The optimal subarray here is [2,4,5,6].

Example 2:

Input: nums = [5,2,1,2,5,2,1,2,5]
Output: 8
Explanation: The optimal subarray here is [5,2,1] or [1,2,5].



Constraints:

	1 <= nums.length <= 105
	1 <= nums[i] <= 104

"""

"""
approach -- 

edge case --> 

if length is 1 
return nums[1]


we need to track unique elemnts and the sum of the elements 

max_sum = 0
running_sum =0  
char_set = 0 

left = 0 
right = 0




for right in range(len(nums)):

	
	while nums[right] in char_set :

		running_sum -= nums[left]

		left += 1


	running_sum += nums[right]

	max_sum = max(running_sum , max_sum)


"""
from typing import List

class Solution:
	def maximumUniqueSubarray(self, nums: List[int]) -> int:
		"""
		The function to find the max sum sub array to erase
		"""

		#edge case 
		if len(nums) == 1 :

			return nums[0]

		#vars
		max_sum , running_sum = 0 , 0 
		left = 0
		char_set = set()


		#loop over the nums
		for right in range(len(nums)) :

			while nums[right] in char_set :

				running_sum -= nums[left]

				char_set.remove(nums[left])

				left += 1

			running_sum += nums[right]

			max_sum = max(running_sum , max_sum)

			char_set.add(nums[right])


		return max_sum



test = [4,2,4,5,6]

test2 = [5,2,1,2,5,2,1,2,5]



sol = Solution()

res = sol.maximumUniqueSubarray(test)


print(res)