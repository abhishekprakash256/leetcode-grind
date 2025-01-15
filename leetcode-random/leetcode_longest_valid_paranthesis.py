"""
Given a string containing just the characters '(' and ')', return the length of the longest 
valid (well-formed) parentheses substring
.
"""

"""
Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0


Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'.

"""

"""
approach -- 
((())) - valid 

use a stack ? 

"()()()" -> 3

"(()" -> 2


if not paranthesis:

	return 0

"((()))"

-> "())))"

()))) -> invalid
()()() -> valid,  


"""

class Solution():

	def longestValidParentheses(self,s):
		"""
		The function to find the invalid string
		passes leetcode
		"""

		#constraints 
		if not s :

			return 0


		if len(s) == 1 :

			return 0

		l,r = 0,0

		mx = 0 

		for para in s:

			if para == "(" :

				l += 1 

			if para == ")" :

				r += 1 


			if l == r :

				mx = max(mx, r*2)

			elif r > l :

				l ,r = 0,0

		
		l,r = 0,0
		#reverse the logic to check 

		for para in reversed(s) :

			if para == ")" :

				l += 1

			if para == "(" :

				r += 1 

			if l == r :

				mx = max(mx , r*2)

			elif r > l :

				l , r = 0,0 


		return mx



