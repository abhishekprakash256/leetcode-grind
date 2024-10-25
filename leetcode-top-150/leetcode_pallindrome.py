"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""


"""

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

"""

class Solution_one(object):
	def isPalindrome(self, s):
		"""
		:type s: str
		:rtype: bool
		""" 
		punc = "~`!@#$%^&*()_-+=[{]}\|;:'\",<.>/?"
		s = s.lower().replace(" ", "")
		for char in punc:
			s = s.replace(char,"")
		return (s == s[::-1])
	


mapper = {"a":1,"b":1,"c":1,"d":1,"e":1,"f":1,"g":1,"h":1,"i":1,"j":1,"k":1,"l":1,"m":1,"n":1,"o":1,"p":1,
               "q":1,"r":1,"s":1,"t":1,"u":1,"v":1,"w":1,"x":1,"y":1,"z":1,"0":1,"1":1,"2":1,"3":1,"4":1,"5":1,
               "6":1,"7":1,"8":1,"9":1}



class Solution(object):
	def isPalindrome(self, s):
		"""
		The function to find pallindrome 
		passes leetcode
		"""

		#vars 
		i = 0 
		j = len(s) - 1

		while i < j :

			left_char = s[i].lower()
			right_char = s[j].lower()

			if (left_char in mapper) and (right_char in mapper) and left_char == right_char:
				i += 1
				j -= 1

			elif (left_char in mapper) and (right_char not in mapper):
				j -= 1 
			
			elif (left_char not in mapper) and (right_char  in mapper):
				i += 1
			
			elif (left_char not in mapper) and (right_char not in mapper):
				i +=1
				j -= 1
			
			elif (left_char in mapper) and (right_char in mapper) and left_char != right_char:
				return False
		
		return True
			

