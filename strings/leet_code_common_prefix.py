"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Input: strs = ["flower","flow","flight"]
Output: "fl"

"""


"""
1.Approach

#base case 
if len(strs) == 1:
	return strs[0]


common_prefix = strs[0]


for i in range(1,len(strs)):

	length = min(len(common_preifx),len(strs[i])):
	
	for idx in range(0,length):

		if common_prefix[idx] != strs[idx]:
			common_prefix = common_prefix[0:strs]

return common_prefix


2.Approach

#base case 
if len(strs) == 1:
	return strs[0]


common_prefix = ""



"""


class Solution:
	def longestCommonPrefix(self, strs):
		"""
		The function to find the longes common prefix 
		"""

		#base case 
		if len(strs) == 1:
			return strs


		#make the common prefix 
		common_prefix = strs[0]

		for i in range(1,len(strs)):

			length = min(len(strs[i]),common_prefix)

			for idx in range(0,length):

				if common_prefix[idx] != strs[i][idx]:
					common_prefix = common_prefix[0:idx]


		return common_prefix
















