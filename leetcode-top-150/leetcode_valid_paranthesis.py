"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

	Open brackets must be closed by the same type of brackets.
	Open brackets must be closed in the correct order.
	Every close bracket has a corresponding open bracket of the same type.

"""

"""



Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

"""


"""

hash map 

mapper =  {'(', ')', '{', '}', '[',']'}


#base case 

if not s :
	return False

if len(s) == 1:
	return False


#make the hashmap

mapper = { '(':')' , '[': ']' , '{' :'}'}


#stack 
stack = []



for paranthesis in s:

	if paranthesis in mappper :

		stack.insert(0,paranthesis)


	else:

		while stack:

			close_paranthesis = stack.pop(0)

			if close_paranthesis != mapper[s] :

				return False

return True



"""



class Solution:
	def isValid(self, s: str) -> bool:
		"""
		The function to find valid paranthesis
		"""

		#base 
		if not s:
			return False

		if len(s) == 1:
			return False

		#make the hashmap
		mapper =  {'(':')', '{': '}', '[':']'}


		#make the stack 
		stack = []

		for para in s:

			if para in mapper:

				stack.insert(0,para)

			else:

				while stack:

					close_para = stack.pop(0)

					if para != mapper[close_para] :

						return False

		return True




sol = Solution()
print(sol.isValid("([])"))

		








