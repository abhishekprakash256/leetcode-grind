"""

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal
substring
consisting of non-space characters only.


"""

"""

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

"""


"""

start the traversal in backward 

edge case 

start with space 

if i == len(s) and i = " ":
	count = 0 

elif i != "" and i <= len(s):
	count += 1

else:
	return count





"""

class Solution:
	def lengthOfLastWord(self, s: str) -> int:
		"""
		The function to find the length of last word
		"""
		pass