"""
Given a string s, find the length of the longest substring without repeating characters.
"""

s = "abcabcbb"
out = 3 

s2 = "bbbbb"
out2 = 1

s3 = "pwwkew"
out3 = 3



# the code is wrong 
class Solution(object):
	def lengthOfLongestSubstring(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		
		#sliding window aproarch 

		if len(s) == 0:
			return 0 

		if len(s) == 1:
			return 1 


		#make hash map 
		mapper = {}

		#make the two pointer 
		i = 0 
		j = i + 1

		#put the first element 
		mapper[s[i]] = i
		max_len = 0

		while j < len(s):

			#start the sliding window 

			if s[j] in mapper:

				temp_len = j - i
				mapper[s[j]] = j
				i = j + 1				
				j +=1
				max_len = max(max_len,temp_len)

			else:
				
				mapper[s[j]] = j
				max_len = max(max_len, j - i + 1)
				j +=1


		return max_len



if __name__ == "__main__":

	sol = Solution()

	res = sol.lengthOfLongestSubstring(s3)

	print(res)