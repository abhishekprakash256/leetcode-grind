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




class Solution(object):
	def longestPalindrome(self, s):
		"""
		:type s: str
		:rtype: str
		"""

		#cover edge cases 
		 
