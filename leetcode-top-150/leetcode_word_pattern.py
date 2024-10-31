"""

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.
"""


"""
Input: pattern = "abba", s = "dog cat cat dog"

Output: true

Explanation:

The bijection can be established as:

'a' maps to "dog".
'b' maps to "cat".
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"

Output: false

Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"

Output: false


"""



class Solution:
	def wordPattern(self, pattern: str, s: str) -> bool:
		"""
		The function to find the word pattern
		passes leetcode
		"""

		#make the list 
		lst = s.split()

		print(lst)

		#base case
		if len(pattern) != len(lst):

			return False
		
		#make hashmap 
		p_to_s = {}
		s_to_p = {}


		#make the matching pattern 
		for i in range(len(lst)):

			if pattern[i] not in s_to_p:
				
				s_to_p[pattern[i]] = lst[i]
				
			else:
                
				if s_to_p[pattern[i]] != lst[i]:

					return False
			

			if lst[i] not in p_to_s :

				p_to_s[lst[i]] = pattern[i]
			
			else:

				if p_to_s[lst[i]] != pattern[i]:
					return False
		
		return True


		


		



