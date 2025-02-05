"""
using the recusion 
"""

class Solution():

	def __init__(self):

		self.result = []

	def helper_dfs(self,idx, temp_lst):
		"""
		The function for helper dfs
		"""

		if len(temp_lst) == self.n - 1 :

			self.result.append(temp_lst)

			return 

		#make the recursive call
		for i in range(idx,self.n) :

			self.helper_dfs(i + 1 , temp_lst + [i])


	def make_combinations(self,n):

		self.n = n

		temp_lst = []

		self.helper_dfs(0, temp_lst)

		return self.result 



sol = Solution()

print(sol.make_combinations(3))



