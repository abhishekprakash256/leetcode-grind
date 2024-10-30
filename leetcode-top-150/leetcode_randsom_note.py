"""

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
"""


"""

Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true

 

"""



"""

#base case 
if not magazine:
	return False


#hash map
ransom_mapper = {}
magazine_mapper = {}




"""



class Solution:
	def canConstruct(self, ransomNote: str, magazine: str) -> bool:
		"""
		The function to make find the not can be make
		"""

		#base case 
		if not magazine:
			return False



		#the hash maps 
		ransom_mapper = {}
		magazine_mapper = {}


		#make the hash map 
		for char in ransomNote:

			if char not in ransom_mapper:

				ransom_mapper[char] = True

			else:

				ransom_mapper[char] = ransom_mapper[char] + 1



		#make the hash map 
		for char in magazine:

			if char not in magazine_mapper:

				magazine_mapper[char] = True

			else:

				magazine_mapper[char] = magazine_mapper[char] + 1



		# match the hash map
		for char in ransom_mapper:

			if char in magazine_mapper:

				if ransom_mapper[char] > magazine_mapper[char] :

					return False

			else:

				return False


		return True
























