"""
Given an array of positive integers nums and a positive integer target, 
return the minimal length of a subarray
 whose sum is greater than or equal to target. 
If there is no such subarray, return 0 instead.
"""

"""
Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0


"""

"""
approach -- 


use a slidng window approach 

app the elemnt and pop the array as soon as sum get's less then add more 


"""



class Solution():

	def minSubArrayLen(self, target ,nums ) :
		"""
		The function to find the minumum sub array 
		"""

		#constarints case 
		
		#if sum is grater than all 
		if sum(nums) < target :

			return 0

		#vars 
		min_len = float("inf")
		queue = [] 
		running_sum = 0 

		for i in range(len(nums)) :

			running_sum += nums[i]

			while running_sum >= target :

				min_len = min(len(queue), min_len)

				val = queue.pop()

				running_sum = running_sum - val

		return min_len












nums2 = [12,28,83,4,25,26,25,2,25,25,25,12]


#sorted [2, 4, 12, 12, 25, 25, 25, 25, 25, 26, 28, 83]


target2 = 213


sol = Solution()

print(sol.minSubArrayLen(target2, nums2))