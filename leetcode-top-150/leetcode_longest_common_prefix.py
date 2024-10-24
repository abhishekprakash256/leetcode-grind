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
        # Base case: if the list is empty, return an empty string
        if not strs:
            return ""

        # Initialize the common prefix to the first string
        common_prefix = strs[0]

        # Loop over the rest of the strings
        for i in range(1, len(strs)):

            # Find the minimum length between the current common prefix and the current string
            length = min(len(common_prefix), len(strs[i]))

            # Check for the common characters
            for j in range(length):
                if common_prefix[j] != strs[i][j]:
                    # Truncate the common prefix at the point of difference
                    common_prefix = common_prefix[:j]
                    break

            # After the inner loop, update the prefix to the length of the current string if needed
            common_prefix = common_prefix[:length]

            # If the common prefix is empty, there's no point in continuing
            if not common_prefix:
                return ""

        return common_prefix

		