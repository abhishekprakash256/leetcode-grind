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




	def generateParenthesis(self, n: int) :
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




#----------------------------------------------------------------------------------------------





class Solution():

	def __init__(self):
		
		self.res_lst = []


	def count_para(self,para):
		"""
		The function to count the parantheis and make it equal on open and close braces
		"""

		count_open = 0
		count_close = 0

		for braces in para:

			if braces == "(":

				count_open += 1

			else :

				count_close += 1 


		if count_open == count_close:
			return True

		else:
			return False



	def helper_dfs(self,para):
		"""
		The dfs helper function
		"""
		
		#base case 
		if len(para) == self.length :

			self.res_lst.append(para)

			return



		#start the resurion
		self.helper_dfs(para + ")")
		self.helper_dfs(para + "(")




	def generateParenthesis(self, n: int):
		"""
		The function to generate the paranthesis  
		"""

		self.length = 2*n
		

		#constarints 
		if n == 1:

			return ["()"]

		#start the recursion 
		self.helper_dfs("(")

		#return the list 
		return self.res_lst







if __name__ == '__main__':
	sol = Solution()
	print(sol.generateParenthesis(3))










































