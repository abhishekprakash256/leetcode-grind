"""
make the permutations in the selection
"""


"""
make the selection of the 

"""







class Solution():

	def __init__(self):
		self.res_lst = []


	def helper(self,start_lst):
		"""
		The helper funciton
		"""

		#base case 
		if len(start_lst) == len(self.nums):
			self.res_lst.append(start_lst[:])
			return None


		for i in self.nums:

			if i in start_lst:

				continue

			start_lst.append(i)

			self.helper(start_lst)

			start_lst.pop()


	def permute(self,nums):
		"""
		The permute function
		"""

		self.nums = nums


		#base case
		if len(nums) == 1:
			return [nums]

		start_lst = []

		self.helper(start_lst)


		return self.res_lst







class Solution():

	def __init__(self):
		self.res_lst = []


	def helper(self,start_lst):
		"""
		The helper funciton
		"""

		#base case 
		if len(start_lst) == len(self.nums):
			self.res_lst.append(start_lst)
			return None


		for i in self.nums:

			if i in start_lst:

				continue

			#start_lst.append(i)

			self.helper(start_lst + [i])

			#start_lst.pop()


	def permute(self,nums):
		"""
		The permute function
		"""

		self.nums = nums


		#base case
		if len(nums) == 1:
			return [nums]

		start_lst = []

		self.helper(start_lst)


		return self.res_lst




sol = Solution()


path = [1,2,3]

sol.dfs(path)


print(sol.res)