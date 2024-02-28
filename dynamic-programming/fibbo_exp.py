"""
find the fibbo series using the different approches 

1,1,2,3,5,8,13

1,2,3,4,5,6
"""





class Solution():

	def __init__(self):

		self.memo = {}


	def fibbo_memo(self,nums):
		"""
		The recursive call for memization
		"""

		if nums == 0 :
			return 0 

		if nums in self.memo:
			return self.memo[nums]


		if nums <=1:
			return nums

		self.memo[nums] = self.fibbo_memo(nums - 1) + self.fibbo_memo(nums - 2)

		return self.memo[nums]



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





if __name__ == "__main__":


	sol = Solution()

	res_rec = sol.fibbo_memo(10)



	print(res_rec)


