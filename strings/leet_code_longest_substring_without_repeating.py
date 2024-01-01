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


s6 = "asjrgapa"
out6 = 6


class Solution():

	#using the brute force approach
	#incorrect 
	def lengthOfLongestSubstring_brute_force_incorrect(self, s):
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

			mapper[s[i]] = True

			for j in range(i+1,len(s)):

				if s[j] not in mapper:

					#debug the code

					mapper[s[j]] = True
					curr = max(curr, len(mapper))

				else:
					mapper = {}
					mapper[s[j]] = True
					curr = len(mapper)

		return curr 


		#works but in O(n^2 timing, 986/987 tests passed)
	def lengthOfLongestSubstring_brute_force(self,s):
		"""
		The function to find the longest string
		without repeating character 
		"""


		#edge cases

		if len(s) == 0:
			return 0 

		if len(s) == 1:
			return 1 


		#make the mapper 
		curr_max = 0

		#start the loop 


		for i in range(len(s)):

			mapper = {}
			mapper[s[i]] = True

			for j in range(i+1,len(s)):

				if s[j] in mapper:

					curr_max = max(curr_max,len(mapper))
					mapper = {}
					mapper[s[j]] = True

				else:
					mapper[s[j]] = True
					curr_max = max(curr_max,len(mapper))


		return curr_max


	#optimize solution
	def lengthOfLongestSubstring(self,s):
		"""
		The fucntion to find the lonhest substring 
		"""


		#set the variables
		char_set = set()
		res,l = 0,0

		for i in range(len(s)):

			while s[i] in char_set:

				#remove the elements 
				char_set.remove(s[l])
				l +=1


			char_set.add(s[i])

			res = max(res, i - l + 1)

		return res 









if __name__ == "__main__":

	sol = Solution()
	res = sol.lengthOfLongestSubstring_brute_force(s4)

	print(res)


