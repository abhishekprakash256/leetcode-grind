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
	"""
	Passess leetcode
	"""

	def __init__(self):
		
		self.res_lst = []

	def count_para(self, para):
		"""
		Check if the parentheses string is valid at this point.
		"""
		count_open = 0

		for braces in para:
			if braces == "(":
				count_open += 1
			else:  # braces == ")"
				count_open -= 1
			
			# If at any point, closing braces exceed opening braces, it's invalid
			if count_open < 0:
				return False

		# Return True if counts are valid
		return count_open == 0




	def helper_dfs(self,para):
		"""
		The dfs helper function
		"""
		
		#base case 
		if len(para) == self.length :
			
			if para[self.length-1] == ")" and self.count_para(para):

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




class Solution_optim:
	"""
	The optimized solution

	"""
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(openP, closeP, s):
            if openP == closeP and openP + closeP == n * 2:
                res.append(s)
                return
            
            if openP < n:
                dfs(openP + 1, closeP, s + "(")
            
            if closeP < openP:
                dfs(openP, closeP + 1, s + ")")

        dfs(0, 0, "")

        return res






if __name__ == '__main__':
	sol = Solution()
	print(sol.generateParenthesis(3))










































