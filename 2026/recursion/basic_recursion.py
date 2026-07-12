"""
The recusion practice basics  
"""



class Solution():

	def factorial(self, nums):
		"""
		The function to find the factorial of the number
		"""

		if nums == 0 :

			return 1


		return  nums * self.factorial(nums - 1)



nums = 5

sol = Solution()

res = sol.factorial(nums)

print(res)