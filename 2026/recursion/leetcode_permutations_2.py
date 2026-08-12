"""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
"""

"""
Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
[1,2,1],
[2,1,1]]

Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

 

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10

"""

"""
approach -- 



"""

class Solution():

	def __init__(self):

		self.res = []


	def _helper(self,  res_lst , used):
		"""
		The function for dfs tree
		"""

		#base case 
		if len(res_lst) == len(self.nums) :

			self.res.append(res_lst)

			return

		for i in range(len(self.nums)) :


			#don't use if in the used
			if used[i] :

				continue

			#the backtrack condition
			if i > 0 and self.nums[i] == self.nums[i - 1] and not used[i - 1]:

				continue

			#when the value is choose
			used[i] = True

			#make the stack
			self._helper(res_lst + [self.nums[i]] , used )

			#undo the use
			used[i] = False



	def permuteUnique(self, nums):
		"""
		The function to find the unique permutations
		"""

		self.nums = sorted(nums)

		used = [False] * len(nums)

		#call the helper function
		self._helper( [] , used)

		#return the result
		return self.res


#testing 

#testing the solution 
if __name__ == '__main__':

	sol = Solution()

	res = sol.permuteUnique( nums = [1,1,2] )

	print(res)


