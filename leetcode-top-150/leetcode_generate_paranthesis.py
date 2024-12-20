"""
Given n pairs of parentheses, write a function to generate 
all combinations of well-formed parentheses.
"""

"""
Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

"""


"""
approach -- 
using a recursion dfs 

#main list
self.combinations_lst =[]



#constraints 

if n == 1 :
	return ["()"]


#length 
self.length = 2*n


self.helper_dfs("")



#base case 
if len(paranthesis) == self.length:

	self.combinations_lst.append(paranthesis)



#recursive call 
left + "("
right + ")"

self.helper_dfs(left+right)
self.helper_dfs(left+right)



"""

class Solution_wrong():

	def __init__(self):

		self.paranthesis_lst = []
		self.para_lst = ["(",")"]


	def helper_dfs(self,temp_para):
		"""
		The helper dfs function
		"""

		#base case 
		if len(temp_para) == self.length :

			self.paranthesis_lst.append(temp_para)

			return


		#make the recursion call 
		for para in self.para_lst:

			if temp_para[0] != ")" :

				self.helper_dfs(temp_para + para)

			else:

				self.helper_dfs(temp_para + "(")




	def generateParenthesis(self, n: int) -> List[str]:
		"""
		The function to generate the dfs 
		"""
		self.length = n*2

		#constraints 
		if n == 1 :
			return ["()"]

		#temp_para
		temp_para = ""

		#make the function call
		self.helper_dfs(temp_para)

		#return the list 
		return self.paranthesis_lst




