"""
Given an array of strings strs, group the 
anagrams
 together. You can return the answer in any order.
"""


"""
Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

"""



"""

res_lst = []
mapper = {}

word.sort()

"""

from typing import List

class Solution:
	def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
		"""
		The function to find the group anagrams
		"""

		#base case 
		if len(strs) == 1 :
			return [[strs[0]]]
		
		#hash map
		mapper = {}


		for word in strs:

			#sort the words
			sorted_word = ''.join(sorted(word))	
			
			if sorted_word not in mapper:

				mapper[sorted_word] = [word]
			
			else:

				mapper[sorted_word].append(word)


		return list(mapper.values())  

