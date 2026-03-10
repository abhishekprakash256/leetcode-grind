"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""

"""

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

 

Constraints:

	2 <= nums.length <= 105
	-30 <= nums[i] <= 30
	The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

"""

"""

approach -- 

make a mutiply array 

from left and right 

two arrays 

then multiply the elemnts to get the value on the spot 

from one spot left and right 


if 0 then , right_prefix [0,len(arra)]

if idx - 1 < 0 
	
	igone left 

if idx + 1 > len(arr) -1 :

	ignore right


"""
from typing import List

class Solution:
	def productExceptSelf(self, nums: List[int]) -> List[int]:
		"""
		The function to find the prefix multiplication array
		"""

		#arry list
		left_prefix = [1] * (len(nums)) 

		right_prefix = [1] * (len(nums))

		ans = [1] * len(nums)

		#make the prefix array
		for i in range(len(nums)) :

			left_prefix[i] = left_prefix[i-1] * nums[i]


		for i in range(len(nums) , 0) :

			right_prefix[i] = right_prefix[i + 1] * nums[i]


		for i in range(len(nums)) :

			if i - 1 < 0 :

				ans[i] = ans[i] * right_prefix[i + 1]

			if i + 1 > len(nums) - 1:

				ans[i] = ans[i] * left_prefix[ i - 1]

			else :

				ans[i] = left_prefix[i-1] * right_prefix[i + 1]


		return ans



if __name__ == "__main__" :

	sol = Solution()

	nums = [1,2,3,4]

	res = sol.productExceptSelf(nums)

	print(res)
