"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 
if needle is not part of haystack
"""

"""
1

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

"""


"""
length = len(s) - (1 + len(needle))
i = 0 

while i < length :

	if needle == haystack[i: i + len(needle)]:
		return i 
	
return - 1


"""


class Solution:
	def strStr(self, haystack: str, needle: str) -> int:
		"""
		The function to find the needle in haystack
		"""

		length =len(haystack) - len(needle) 
		i = 0 

		while i <= length:

			if needle == haystack[i:i + len(needle)]:
				return i

			i += 1
		
		return - 1


