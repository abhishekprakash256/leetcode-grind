"""
Make the susbsets with two approaches 

"""









class Solution_recursion():

	def __init__(self):

		self.results = []

	def _helper_dfs(self,idx,temp_lst):
		"""
		The helper function to make the combinations
		"""
		#append in list
		self.results.append(temp_lst)

		#base case

		for i in range(idx,len(self.nums)) :

			self._helper_dfs(i + 1 , temp_lst + [self.nums[i]])
		


	def main_fun(self,nums):
		"""
		The main function to make the combinations lists
		"""

		self.nums = nums

		#conbstraint case 
		if len(self.nums) == 0 :
			return self.results

		temp_lst = []
		idx = 0 

		self._helper_dfs(0,[])

		return self.results



class Solution_backtracking():

	def __init__(self):

		self.results = []

	def _helper_dfs(self,idx,temp_lst):
		"""
		The helper function to make the combinations
		"""
		#append in list
		self.results.append(temp_lst[:])  #make a copy here

		#base case

		for i in range(idx,len(self.nums)) :

			temp_lst.append(self.nums[i])

			self._helper_dfs(i + 1 , temp_lst)

			temp_lst.pop()
		


	def main_fun(self,nums):
		"""
		The main function to make the combinations lists
		"""

		self.nums = nums

		#conbstraint case 
		if len(self.nums) == 0 :
			return self.results

		temp_lst = []
		idx = 0 

		self._helper_dfs(0,[])

		return self.results

















test_arr = [1,2,3]

sol_rec = Solution_recursion()

sol_back = Solution_backtracking()

print(sol_rec.main_fun(test_arr))

print(sol_back.main_fun(test_arr))
