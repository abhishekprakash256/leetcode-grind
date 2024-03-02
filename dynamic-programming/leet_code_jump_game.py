"""

You are given an integer array nums. You are initially positioned at the array's first index, 
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

"""


nums = [2,3,1,1,4]
out = True 



nums2 = [3,2,1,0,4]
out2 = False




"""
make the algo -- 



"""


class Solution():

	def canJump_brute_force_incorrect(self,nums):
		"""
		The function to find the brute force soln of can jump 
		"""

		if len(nums) == 1:

			if nums[0] == 0 or nums[0] ==1 :
				return True

		for i in range(len(nums) - 1):

			for j in range(1,nums[i]+1):

				#print(i+j)

				if i + j == len(nums)- 1:
					return True 


		return False


	def canJump_dp(self,nums):
		"""
		The function to find the jumps possible
		"""

		#base casese
		if len(nums) == 1:

			if nums[0] == 0 or nums[0] ==1 :
				return True


		



if __name__ == '__main__':
	
	sol = Solution()

	print(sol.canJump_brute_force(nums2))