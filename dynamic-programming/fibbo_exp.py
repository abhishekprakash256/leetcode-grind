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


	def fibbo_dynamic(self,nums):
		"""
		The function to make the fibbonchie using dp

		"""

		dp = [0]*(nums + 1)

		dp[1], dp[2] = 1,1

		for i in range(2,nums + 1):

			dp[i] = dp[i-1] + dp[i-2]

		return dp[nums]



if __name__ == "__main__":


	sol = Solution()

	res_rec = sol.fibbo_dynamic(40)



	print(res_rec)


