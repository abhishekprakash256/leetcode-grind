"""
Given an integer array nums of length n and an integer target, find 

three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

"""


"""

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).


Constraints:

3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104

"""

"""
approach -- 

sort 

-4,-1, 1,2 -> 

use one value and pinter left and right to move 

l , r 

brute force approach -- 

get a min value , 

result_val = float("inf")

if target - curr_val = curr_min

curr_min = target - curr_val 

result_val = min(curr_min,result_val)



"""

class Solution():

	def threeSumClosest(self,nums, target) :
		"""
		The function to find the closest sum 
		"""

		#constarints
		if len(nums) == 3 :

			return sum(nums)

		#sort the nums 
		nums.sort()

		#min value 
		min_value = float("inf")

		#make the loop 
		for i in range(len(nums)- 2):

			l = i + 1 
			r = len(nums) - 1 

			while l < r :

				cur_sum = nums[i] + nums[l] + nums[r]

				if abs(cur_sum - target) < abs(target - min_value) :

					min_value = cur_sum


				if cur_sum == target :

					return cur_sum

				elif cur_sum < target :

					l += 1 
				
				else :

					r -= 1

		return min_value





sol = Solution()

print(sol.threeSumClosest([-1,2,1,-4], 1))