"""
Given a string containing digits from 2-9 inclusive, return all possible letter
 combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below.

Note that 1 does not map to any letters.
"""


"""
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

"""

"""

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
"""

"""
approach -- 

make a dict 

mapper = { 2: "abc" ,3: "def" , 4:"ghi" , 5:"jkl", 6:"mno" , 7:"pqrs", 8:"tuv", 9:"wxyz"}
res_lst = []


base case 
if not input digit:
	return []


#looks like a tree 

#do dfs and return all the possiblities 

#and append it in the list with all output

steps 

first make tree
then do dfs 

empty string 

combination = ""

base fun

for i in range(len(digit))
	
	self.helper_dfs(digits[i],i ,combination)

return self.combination_lst


def helper_dfs(char,i, combination):

	#base case 
	if i == len(digits) - 1 :
		
		self.combinations_lst.append(combination)
		return None

	#add the values in string

	for j in mapper[char]:
		
		combination += "j"

		self.helper_dfs( digit[i+1],i+1, combination)

"""



class Solution:

	def __init__(self):

		self.combinatons_lst = []
		self.mapper = = { 2: "abc" ,3: "def" , 4:"ghi" , 5:"jkl", 6:"mno" , 7:"pqrs", 8:"tuv", 9:"wxyz"}


	def helper_dfs(char,i,combination):
		"""
		The dfs helper function
		"""

		#base case 
		if i == len(self.digits) - 1 :

			self.combinatons_lst.append(combination)

			return None

		#add the value in the string
		for j in self.mapper[char]:

			combination += j

			self.helper_dfs(self.digits[i+1],i+1,combination)





	def letterCombinations(self, digits: str) -> List[str]:
		"""
		The function to find all the possible combinations 
		"""

		self.digits = digits

		#base case 
		if not digits:
			return self.combinatons_lst

		#initial input for combination
		combination = ""

		#start the traversal 
		for i in range(len(self.digits)) :

			self.helper_dfs(self.digits[i],i,combination)


		return self.combinatons_lst



