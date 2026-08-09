"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
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

 

Constraints:

1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40


"""

"""

approach 

make sum and carry the sum 

#discard condition

if sum > target:

	return 


if sum == target :

	res.append(sum_lst)


for i in candidates : 

	self._helper(sum + i , sum_lst + [i])


"""

from typing import List




class Solution:
	def __init__(self):

		self.res = []


	def _helper(self,curr_sum , sum_lst):
		"""
		The funciton to find the sum by backtrack
		"""

		#base case
		if curr_sum > self.target :

			return


		#base case 
		if curr_sum == self.target :

			self.res.append(sum_lst)

			return

		#make the recursions all
		for i in self.candidates : 

			self._helper(curr_sum + i , sum_lst + [i])



	def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
		"""
		The function to find the combination sum for target 
		"""

		#target sum
		self.target = target

		#the canidates list
		self.candidates = candidates

		#call the backtrack function
		self._helper(curr_sum = 0 , sum_lst = [])

		#return the results
		return self.res




#testing the solution 



if __name__ == '__main__':

	sol = Solution()

	res = sol.combinationSum(candidates = [2,3,6,7], target = 7)

	print(res)




























		
