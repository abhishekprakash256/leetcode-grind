"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

"""

"""
Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]

Constraints:

1 <= n <= 8


"""


"""
approach -- 

using the approch , left and right and balance,

if right is open then discard, if left is open then discard


"""


from typing import List



class SolutionWrong:
	def __init__(self):

		self.res = []
		self.para_lst = ["(",")"]


	def _helper(self,i, para_str):
		"""
		The function to make the dfs
		"""

		#testing the para
		#print(para_str)


		#make the base case
		if self.n*2 == len(para_str) :

			#discard case
			if para_str[( 2*self.n ) - 1 ] == "(" :

				return

			self.res.append(para_str)

			return


		#make the stack
		for para in self.para_lst:

			#call the helper function
			self._helper(i + 1, para_str + para)




	def generateParenthesis(self, n: int) -> List[str]:
		"""
		The function to make the paranthessis
		"""

		self.n = n

		#make the str
		para_str = "("

		#call the helper
		self._helper(0, para_str )

		return self.res









#testing the other solutions --- 

class Solution:
	def __init__(self):

		self.res = []
		self.para_lst = ["(",")"]


	def _helper(self, left , right , para_str):
		"""
		The function to make the dfs
		"""

		#testing the para
		#print(para_str)


		#make the base case
		if self.n*2 == len(para_str) :

			self.res.append(para_str)

			return


		#make the stack
		if left < self.n :

			self._helper( left + 1 , right + 0,  para_str + "(")


		if right < left : 

			self._helper( left + 0 , right + 1 ,para_str + ")")






	def generateParenthesis(self, n: int) -> List[str]:
		"""
		The function to make the paranthessis
		"""

		self.n = n

		#make the str
		para_str = ""

		#call the helper
		self._helper(0 , 0, para_str )

		return self.res





#testing the solution 



if __name__ == '__main__':

	sol = Solution()

	res = sol.generateParenthesis(3)

	print(res)









