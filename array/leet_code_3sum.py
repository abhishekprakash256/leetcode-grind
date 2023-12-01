"""
find 3 sum triplte in the array 
"""

#test case 

nums = [-1,0,1,2,-1,-4]

out = [[-1,-1,2],[-1,0,1]]



class Solution:

	def threeSum_incorrect(self,nums):
		"""
		find the sum that equals to zero
		"""

		res_lst = []

		nums.sort()

		if len(nums) < 3:

			return False

		for i in range(len(nums)):

			l,r = i+1, len(nums) - 1

			while l < r:

				sum = nums[i] + nums[l] + nums[r]

				if sum == 0 :
		
					res_lst.append([nums[i],nums[l],nums[r]])
					l +=1

				elif sum > 0:

					r -=1

				else:

					l +=1

		return res_lst





if __name__ == "__main__":

	sol = Solution()

	res = sol.threeSum(nums)

	print(res)