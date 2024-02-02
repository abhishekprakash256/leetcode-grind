"""
leet code the longest pallindrome substring 
"""

s = "abcabcbb"
out = 3


s2 = "bbbbb"
out2 = 1

s3 = "pwwkew"
out3 = 3 


"""
Algo 

two pointer approach 
sliding window 
set to store my unique elements 

l = 0 
r = l+=1
queue = set()
	
"""


class Solution:
	def lengthOfLongestSubstring(self, s):
		"""
		The function to find the longest pallindrome sustring 
		"""

		char_set = ()
		res, r = 0,0 

		for i in range(len(s)):

			while s[i] in char_set:
				char_set.remove(s[l])

				l+=1
			
			char_set.add(s[i])

			res = max(res,i - l + 1)
		
		return res



