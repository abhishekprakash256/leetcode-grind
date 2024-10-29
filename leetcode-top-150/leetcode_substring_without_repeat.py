"""
Given a string s, find the length of the longest 
substring
 without repeating characters.
"""

"""
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""


"""

#base case 
if len(s) == 1:
    return 1 


i = 0
max_len = float("-inf")


for j in range(1, len(s)):

    max_len = max(( j - i + 1),max_len)
    
    while s[j] in s[i:j+1]:
        
        i += 1

return max_len


"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Function to find the length of the longest substring without repeating characters.
        passes leetcode 
        """

        # Edge case for empty string
        if not s:
            return 0

        # Variables for sliding window
        i = 0
        max_len = float("-inf")
        char_set = set()

        # Loop through the string
        for j in range(len(s)):
            # If s[j] is already in the set, remove characters from the start of the window until s[j] is not in the set
            while s[j] in char_set:
                char_set.remove(s[i])
                i += 1

            # Add the current character to the set and update the maximum length
            char_set.add(s[j])
            max_len = max(max_len, j - i + 1)

        return max_len

        
