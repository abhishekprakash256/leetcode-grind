"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some 
(can be none) of the characters without disturbing the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).

"""

"""
Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false


"abcde"
"aec"


"""

"""



if not s:
	retun False

#vars 
i = 0 
j = 0 


length = len(t)
count = 0 
while i < len(t):

	if t[i] == s[j]:
		j += 1
		count += 1

	i += 1 
	
if count == len(t) : 
	return True
else:
	return False


"""

class Solution:
	def isSubsequence(self, s: str, t: str) -> bool:
		"""
		The function to find the subsequince exists 
		passes leetcode
		"""

		#base case 
		if not s :
			return True
	
		#vars 
		count , i , j = 0,0,0

		#start the loop 
		while i < len(t) and j < len(s):

			if t[i] == s[j]:
				j += 1
				count += 1
			
			i += 1
		
		if count == len(s):
			return True
		else:
			return False
			



