"""

The frequency of an element is the number of times it occurs in an array.

You are given an integer array nums and an integer k. In one operation, 

you can choose an index of nums and increment the element at that index by 1.

Return the maximum possible frequency of an element after performing at most k operations.
"""

"""


Example 1:

Input: nums = [1,2,4], k = 5
Output: 3
Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
4 has a frequency of 3.

Example 2:

Input: nums = [1,4,8,13], k = 5
Output: 2
Explanation: There are multiple optimal solutions:
- Increment the first element three times to make nums = [4,4,8,13]. 4 has a frequency of 2.
- Increment the second element four times to make nums = [1,8,8,13]. 8 has a frequency of 2.
- Increment the third element five times to make nums = [1,4,13,13]. 13 has a frequency of 2.

Example 3:

Input: nums = [3,9,6], k = 2
Output: 1

 

Constraints:

	1 <= nums.length <= 105
	1 <= nums[i] <= 105
	1 <= k <= 105




"""



"""

approach --> 

make the cost function 

track the window and the cost function 

then move the pointer of the sliding window based on reqs

"""
from typing import List


class Solution:
	def maxFrequency(self, nums: List[int], k: int) -> int:
		"""
		The function to find the frequency of frequent elemnts
		"""

		#vars
		max_window = 0

		#ptrs 
		l , r = 0 , 0

		#sort the array
		nums.sort()

		print(nums)

		#running sum
		running_sum = 0

		#start the loop
		while r <= len(nums) - 1  :

			#get the runnning sum
			running_sum += nums[r]

			#get the cost 
			cost = nums[r] * (r-l) - running_sum

			print(cost)

			while cost > k :


				running_sum -= nums[l]

				l += 1

			if cost == k :

				max_window = max(max_window , r - l )

			r += 1


		return max_window




nums = [1,2,4]
k = 5


if __name__ == "__main__" :

	sol = Solution()

	res = sol.maxFrequency(nums, k)

	print(res)
		

