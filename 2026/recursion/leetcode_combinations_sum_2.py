"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
"""


"""

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]

 

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30

"""

"""

approach -


use the index to start the iter 

carry the sum , use the index , 

add the sum list if the sum is correct 

not add if greater 

"""

from typing import List





class Solution:
	def __init__(self) :

		self.res = []


	def _helper(self, start , curr_sum , sum_lst ):
		"""
		The helper function for the backtracking
		"""

		#base case 
		if curr_sum > self.target :

			return

		#if the sum is equal
		if curr_sum == self.target : 

			self.res.append(sum_lst)

		#make the stack calls
		for i in range(start , len(self.candidates)) : 

			# Skip duplicates: If the current element is the same as the previous one, skip it
			if i > start and self.candidates[i] == self.candidates[i - 1]:
				
				continue

			self._helper(i + 1 , curr_sum + self.candidates[i], sum_lst + [self.candidates[i]])





	def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
		"""
		The function to find the combinations of the sum
		"""

		#target sum 
		self.target = target

		#the canidates list
		self.candidates = sorted(candidates)

		#call the helper functin
		self._helper(0 , 0 , [])

		#return the results
		return self.res





#testing the solution 
if __name__ == '__main__':

	sol = Solution()

	res = sol.combinationSum2(candidates = [2,5,2,1,2], target = 5 )

	print(res)


	













































