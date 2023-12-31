"""
Given a string s, find the length of the longest substring without repeating characters.
"""


s = "abcabcbb"
out = 3 


s2 = "tttt"
out2 = 1


s3 = ""
out3 = 0


s4 = "abbbbcx"
out4 = 3 


s5 = "au"
out5 = 2

class Solution(object):

	#using the brute force approach
	#incorrect 
	def lengthOfLongestSubstring_brute_force(self, s):
		"""
		:type s: str
		:rtype: int
		"""

		#edge case handling 

		#empty or one letter 
		if len(s) == 0 :
			return 0

		if len(s) == 1:
			return 1


		curr = 0
		mapper = {}


		#loop for iteration 
		for i in range(len(s)):

			mapper[i] = True

			for j in range(i+1,len(s)):

				if s[j] not in mapper:
					
					mapper[s[j]] = True
					curr = max(curr, len(mapper))

				else:
					mapper = {}
					mapper[s[j]] = True

		return curr 



if __name__ == "__main__":

	sol = Solution()
	res = sol.lengthOfLongestSubstring_brute_force(s)

	print(res)


