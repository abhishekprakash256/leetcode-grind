"""
find the fibbo series using the different approches 

1,1,2,3,5,8,13

1,2,3,4,5,6
"""





class Solution():

	def __init__(self):

		self.memo = {}

	def fibbo_recursive(self,nums):
		"""
		The function to find the fibbonachi series of the number using 
		recursion
		"""

		#base case 

		if nums == 0:
			return 0 

		if nums == 1 or nums == 2 :
			return 1 


		#the recursive call 
		return self.fibbo_recursive(nums - 1) + self.fibbo_recursive(nums - 2 )


	def fibbo_recursive_memo(self,nums):
		"""
		The function to find the fibbo sequence using memoziation recursion
		"""

		for nums in self.memo:
			return memo[nums]

		if nums <=1:
			return nums


		self.memo[nums] = self.memo()












if __name__ == "__main__":


	sol = Solution()

	res_rec = sol.fibbo_recursive_memo(40)

	print(res_rec)


