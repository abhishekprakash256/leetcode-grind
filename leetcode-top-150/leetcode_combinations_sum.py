"""
Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers sum to 
arget. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.
 Two combinations are unique if the 
frequency
 of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up 
to target is less than 150 combinations for the given input.
"""

"""
Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []

"""


"""
approach -- 

using recursion and repetation 

#base case for recurions 
if sum(temp_lst) > target :
	return 

if sum(temp_lst) == target :

	self.main_lst.append(temp_lst)
	return


for i in self.canidates:

	self.helper_dfs(temp_lst + [i])


avoid the dupliaction repetation  ? 




"""



class Solution():
	"""
	Pasees leet code 
	"""

	def __init__(self):

		self.combinatons_lst = []
		self.mapper = {}


	def helper_dfs(self,temp_lst , unique):
		"""
		The function to make the dfs
		"""
		#base case 
		if sum(temp_lst) == self.target :

			self.combinatons_lst.append(temp_lst)
			return

		#if the sum is more 
		if sum(temp_lst) > self.target:

			return

		#start the recursive call
		for i in self.candidates :

			new_unique = tuple(sorted(temp_lst + [i]))

			if new_unique not in self.mapper :

				self.mapper[new_unique] = True

				self.helper_dfs(temp_lst + [i] , new_unique)



	def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
		"""
		The function to form the combination sum 
		"""

		self.candidates = candidates
		self.target = target


		#constraints 

		if len(candidates) == 1 and candidates[0] == self.target:
			return [candidates]

		#the set for tuple
		unique = tuple()

		#the temp lst
		temp_lst = []

		#the recursive iteration
		self.helper_dfs(temp_lst , unique)

		#return the list 
		return self.combinatons_lst

