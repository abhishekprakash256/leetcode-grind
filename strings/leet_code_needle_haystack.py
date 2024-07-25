"""

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.


"""


"""
algo 
1. One to match on to search 
two poniter 


def strStr()
	for i in range(0,len(haystack)- len(needle)):

		if haystach[i:len(needle)] == needle:
			return i 

	return False








"""
haystack = "hello"
needle = "ll" 


class Solution:
	def strStr(self, haystack: str, needle: str) -> int:
		"""
		The function to find the needle in haystack
		passed leetcode
		"""

		for i in range(0,len(haystack) - len(needle)):


			print(haystack[i:len(needle)])

			if haystack[i:i+len(needle)] == needle:
				
				return i


		return -1


if __name__ == '__main__':
	sol = Solution()
	res = sol.strStr(haystack,needle)

	print(res)