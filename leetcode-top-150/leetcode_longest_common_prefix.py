"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

"""

Input: strs = ["flower","flow","flight"]
Output: "fl"


Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


"""


"""
#base case 
for word in strs:
	if len(word) == 0:
		return ""


common_prefix = strs[0]

for i in range(1,len(strs) - 1 ):

	length = min(len(common_prefix), len(strs[i]))

	for j in range(0,length - 1 ):

		if common_prefix[j] != strs[i][j]:
			common_predix = common_preifx[j-1]

return common_prefix



"""


class Solution(object):
	def longestCommonPrefix(self, strs):
		"""
		:type strs: List[str]
		:rtype: str
		"""
		
		

		