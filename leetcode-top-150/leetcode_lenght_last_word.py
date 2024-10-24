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

space = True

if s[i] != "" and i == len(s)-1:
	count +=1
	space = False

elif s[i] == " " and space and i < len(s) - 1:
	count += 0 


elif s[i] !=" " and s < len(s) - 1:
	count += 1  

else:
	return count 


"""

class Solution_wrong:
	def lengthOfLastWord(self, s: str) -> int:
		"""
		The function to find the length of last word
		"""

		#vars 
		count = 0
		space = True
		i = len(s) - 1  

		#base case 
		if len(s) == 1 :
			return 1

		#star the loop

		while i > -1 :

			if s[i] != " " and i <= len(s) - 1 :

				count += 1 
				space = False

			elif s[i] == " " and space and i <= len(s) - 1 :
				count += 0

			elif s[i] != " " and i <= len(s) - 1 and not space:
				count += 1

			else :
				return count + 1

			i -= 1




class Solution:
	def lengthOfLastWord(self, s: str) -> int:
		"""
		The function to find the length of the last word 
		Leetcode accepted beats 100% 
		"""

		#base case
		if len(s) == 1:
			if s[0] != " ":
				return 1

			else :
				return 0 


		#vars
		count = 0
		space = True
		i = len(s) - 1


		#star the loop
		while i > -1 :

			if s[i] != " ":

				while i > -1:

					count +=1

					if s[i] == " ":
						return count - 1

					i -= 1

			i -= 1

		return count 









sol = Solution()

print(sol.lengthOfLastWord("luffy is still joyboy"))













		


		





