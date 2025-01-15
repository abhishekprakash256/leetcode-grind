"""
Given an integer array nums that may contain duplicates, return all possible
subsets
(the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""

"""
Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:

Input: nums = [0]
Output: [[],[0]]


Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10

"""

"""
approach  --- 

using recursion 

result is a set 

check every time we add a list 

add a empty list as well 

increase the i 

"""


nums = [1,2,2]

output = [[],[1],[1,2],[1,2,2],[2],[2,2]]


class Solution_wrong():

	def __init__(self):

		self.result = []

	def helper_dfs(self,i, temp_lst) :
		"""
		The helper dfs for making the subsets 
		"""

		#base case 
		if len(temp_lst) == len(self.nums) :

			self.result.append(temp_lst)

			return

		if temp_lst in self.result:

			return

		#make the recursion call
		for j in range(i,len(self.nums)):

			if temp_lst not in self.result :

				self.result.append(temp_lst +[self.nums[j]])

				self.helper_dfs(i+1,temp_lst + [self.nums[j]])

			 

	def subsetsWithDup(self,nums) :
		"""
		The function to find the subsets 

		"""
		self.nums = nums

		#constarints 
		if len(nums) == 1 :

			return [[],[nums[0]]]


		#make the vars 
		i = 0
		temp_lst = []

		self.helper_dfs(i,temp_lst)

		self.result.append([])

		return self.result









class Solution_wrong2():

	def __init__(self):

		self.result = []

	def helper_dfs(self,i,temp_lst):
		"""
		The helper dfs function for making the search
		"""

		#base case 
		if temp_lst in self.result :

			return

		if len(temp_lst) > len(self.result):

			return

		#make the recursion 
		for j in range(i,len(self.nums)) :

			temp_lst = temp_lst + [self.nums[j]]

			#print(temp_lst)

			self.result.append(temp_lst)

			self.helper_dfs(j + 1 , temp_lst + [self.nums[j]])



	def subsetsWithDup(self,nums):
		"""
		The function to find the subsets 
		"""
		
		self.nums = nums

		#constarints 
		if len(self.nums) == 1 :

			return [[],[self.nums[0]]]


		#make the vars 
		i = 0
		temp_lst = []

		self.helper_dfs(i,temp_lst)

		self.result.append([])

		return self.result





class Solution_:
    def __init__(self):
        self.result = []

    def helper_dfs(self, nums, index, temp_lst):
        """
        Helper function for depth-first search.
        """
        # Add the current subset to the result
        self.result.append(temp_lst)

        # Iterate through the remaining elements
        for i in range(index, len(nums)):
            # Skip duplicates
            if i > index and nums[i] == nums[i - 1]:
                continue
            # Recurse with the next element
            self.helper_dfs(nums, i + 1, temp_lst + [nums[i]])

    def subsetsWithDup(self, nums):
        """
        Function to find subsets, including duplicates handling.
        """
        # Sort the array to handle duplicates easily
        nums.sort()
        #self.result = []  # Reset result for fresh computation
        self.helper_dfs(nums, 0, [])
        return self.result



class Solution():

	def __init__(self):

		self.result = set()

	def helper_dfs(self,i,temp_lst) :
		"""
		The helper dfs function to add in the list
		"""

		#base case 
		self.result.add(tuple(temp_lst))

		#do the recursion call
		for j in range(i,len(self.nums)):

			self.helper_dfs(j+1,temp_lst + [self.nums[j]])



	def subsetsWithDup(self,nums) :
		"""
		The main funciton 
		"""
		nums.sort()
		self.nums = nums


		if len(nums) == 1:

			return [[],[nums[0]]]


		#make the vars 
		i = 0 
		temp_lst = []

		self.helper_dfs(i,temp_lst)

		return [list(subset) for subset in self.result]



sol = Solution()
print(sol.subsetsWithDup(nums))
