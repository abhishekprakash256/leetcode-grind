"""
123 -> 1 ,2 , 3 ,12, 13, 23 , 123  

"""


class Solution():

	def __init__(self):

		self.result_combinations = []

		self.result_permutations = []

		self.result_all = [] 


	def helper_dfs_combinations(self,i,temp_lst):
		"""
		The function to make the dfs call
		"""

		#base case 


		#make the recursive call
		for j in range(i,self.n + 1) :

			if j not in temp_lst:

				#add in the temp list
				self.result_combinations.append(temp_lst + [j])

				#make the function call
				self.helper_dfs_combinations(j+1,temp_lst + [j])



	def make_combination(self,n):
		"""
		The function to make the result list
		"""

		self.n = n 

		#constarints case 
		if self.n == 0 :

			return []

		if self.n == 1 :

			return [[1]]

		#start the temp
		i = 1
		temp_lst = [] 

		#make the recursive calls
		self.helper_dfs_combinations(i,temp_lst)

		return self.result_combinations




	def helper_dfs_permutations(self,temp_lst):
		"""
		The function to make the possible permutations
		"""

		#base case 

		#if the length is equal
		if len(temp_lst) == self.n :

			self.result_permutations.append(temp_lst)


		#make the recursion calls

		for i in range(1,self.n+1):

			if i not in temp_lst :

				self.helper_dfs_permutations(temp_lst + [i])



	def make_permutations(self,n):
		"""
		The function to make all the permutations
		"""

		self.n = n 

		if self.n == 0 :

			return []


		if self.n == 1 :

			return [[1]]

		temp_lst = []

		#make the permutations helper function call
		self.helper_dfs_permutations(temp_lst)

		return self.result_permutations



	def helper_dfs_all(self,temp_lst):
		"""
		The functon to make all the three digit combinations
		"""

		#base case 

		#if the length is equal

		if len(temp_lst) == self.n :

			self.result_all.append(temp_lst)

			return

		#make the recurisve call
		for i in range(1,self.n+1) :

			self.helper_dfs_all(temp_lst + [i])

	

	def make_all(self,n):
		"""
		The function to make all the 3 digit combinations

		"""
		self.n = n

		if self.n == 0 :

			return []

		if self.n == 1 :

			return [[1]]

		#make the list
		temp_lst = []

		#make the recursive call to the function
		self.helper_dfs_all(temp_lst)

		#return the list
		return self.result_all




	








sol = Solution()

print(sol.make_combination(3))

print(sol.make_permutations(3))

print(sol.make_all(3))



