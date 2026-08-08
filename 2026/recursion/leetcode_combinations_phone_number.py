"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""

"""

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:

Input: digits = "2"
Output: ["a","b","c"]

Constraints:

1 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].


"""



"""

approach -- 




make the decision tree with the digits going and the the brach as the combinations of the alpahbet taken

all the digits and alpahabet will store in hash map 


mapping = {
	'2': 'abc',
	'3': 'def',
	'4': 'ghi',
	'5': 'jkl',
	'6': 'mno',
	'7': 'pqrs',
	'8': 'tuv',
	'9': 'wxyz'
}



"""

from typing import List

class Solution:

	def __init__(self):

		self.res = []

		self.mapper = {
			'2': 'abc',
			'3': 'def',
			'4': 'ghi',
			'5': 'jkl',
			'6': 'mno',
			'7': 'pqrs',
			'8': 'tuv',
			'9': 'wxyz'
		}



	def _helper(self, i , res_str):
		"""
		The helper function for the dfs
		"""

		#base case 
		if i == len(self.digits) :

			self.res.append(res_str)

			return


		#make combinations
		for char in self.mapper[self.digits[i]] :

			self._helper(i + 1 , res_str + char)







	def letterCombinations(self, digits: str) -> List[str]:
		"""
		The function to find the combinations of the  numbers
		"""

		self.digits = digits

		#make the res
		res_str = ""

		#call the helper function
		self._helper(0,res_str)

		#return the result
		return self.res






#testing the code 





if __name__ == '__main__':

	sol = Solution()

	res = sol.letterCombinations("23")

	print(res)




