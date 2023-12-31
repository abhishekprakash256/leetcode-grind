"""
The longest substring without repeating charaters 
"""

#test case 
string = "babad"
out = "bab" #aba

string2 = "abaabtc"
out2 = "baab"

string3 = ""
out3 = ""


string4 = "tttt"
out4 = "tttt"


string5 = "tatttt"
out5 = "tttt"

string6= "ac"
out6 = ""


class Solution(object):

	def checkPallindrome(self,left, right,s):
		"""
		The function to check the pallindrome 
		"""

		while left <= right :

			if s[left] != s[right]:
				return False

			left +=1
			right -=1

		return True 


	#this is brute force approach 
	#take the o(n^2) time to run 
	def longestPalindrome_brute_force(self, s):
		"""
		:type s: str
		:rtype: str
		"""

		#cover edge cases 
		if len(s) <=1 :
			return s

		#initilaize the variables 
		curr = 0

		#cover the edge case of no pallindrome string 
		max_str = s[0]

		#start the loop to check 
		for left in range(len(s)):

			for right in range(left +1, len(s)):

				if self.checkPallindrome(left,right,s) == True:

					temp_len = ((right - left) +1)

					print(temp_len)

					if temp_len > curr: 

						curr = temp_len
						max_str = s[left:right+1]

		return max_str




	def longestPalindrome(self,s):
		"""
		The function to find the longest pallindrome
		using sliding window 

		"""
		



		pass

if __name__ == "__main__":
	
	sol = Solution()

	res = sol.longestPalindrome_brute_force(string6) 

	print(res)
