"""
Given two integers n and k, return all possible combinations of k numbers chosen 

from the range [1, n].

You may return the answer in any order.

 
"""


"""
Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.


"""


"""
1,2,3,4


#base case 
if n == 1 and k == 1:
	return [[1]]


#in the last add as int from string

self.helper_dfs(1,"")

return self.combinatons_lst






#base case for termination
if len(combination) == k:
	combination_lst.append(combination)
	return 


#iterarte 
for j in range(i,n+1):

	self.helper_fun(i+1,combinations+i)




"""


class Solution():
	"""
	passes leet code 
	"""


	def  __init__(self):

		self.combinatons_lst = []



	def helper_dfs(self,i,temp_lst):
		"""
		The function to do the dfs in the letters
		"""

		#base case 
		if len(temp_lst) == self.k :

			self.combinatons_lst.append(temp_lst)
			return


		#start the loop for recursion
		for j in range(i,self.n+1):

			temp_lst.append(j)
			#recursion call

			self.helper_dfs(j+1,temp_lst)
			temp_lst.pop()




	def combine(self, n: int, k: int) :
		"""
		The function to combine the letters of int
		"""

		self.k = k 
		self.n = n

		#base case 
		if n == 1 and k == 1 :
			return [[1]]


		temp_lst = []
		#start the recursion
		self.helper_dfs(1,temp_lst)

		#return the combinations list
		return self.combinatons_lst



class Solution1:
	"""
	passes leet code no popping is used 
	"""
    def __init__(self):
        self.combinations_lst = []

    def helper_dfs(self, i, temp_lst):
        # Base case: if we have k elements, add this combination to results
        if len(temp_lst) == self.k:
            self.combinations_lst.append(temp_lst)  # Directly use temp_lst
            return
        
        # Iterate over possible numbers from i to n
        for j in range(i, self.n + 1):
            # Recur with temp_lst + [j], creating a new list for the next call
            self.helper_dfs(j + 1, temp_lst + [j])

    def combine(self, n, k):
        self.k = k
        self.n = n
        self.helper_dfs(1, [])
        return self.combinations_lst