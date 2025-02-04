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
sorting 

1,2,2,3,3,4

sorting helps 

edge case 

if sum(nums) < target :

	return 0 

if I have two do miniumum start from back 

sum += nums >= target 
 retrun r 

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


		#if all sum is equal 
		if sum(nums) == target :

			return len(nums)

		






nums2 = [12,28,83,4,25,26,25,2,25,25,25,12]

target2 = 213


sol = Solution()

print(sol.minSubArrayLen(target2, nums2))