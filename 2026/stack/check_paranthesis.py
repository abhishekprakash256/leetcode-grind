"""
check the paranthesis order in the stack
"""


class Solution():

	def isValid(self, para) :
		"""
		The function to check the paranthesis if that form the order
		"""

		mapper = {
		")" : "(",
		"}": "{",
		"]": "["
		}

		stack = []

		#iterate over the paranthesis
		for i in para :

			if i in "([{":
				
				stack.append(i)


			else :

				if not stack :

					return False

				
				if stack[-1] != mapper[i] :

					return False

				stack.pop()


		return len(stack) == 0