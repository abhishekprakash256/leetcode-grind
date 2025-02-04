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
using a set and two pointer ? 

max_length = "-inf"

use two pointer in side by side and slide per max and get the stack length 

"""

class Solution():
    """
    clean code passes leet code
    """

    def lengthOfLongestSubstring(self, s: str):
        """
        The function to find the max length of substring without repeat
        """

        #constarints case 
        
        #no string 
        if not s :

            return 0 

        #only one len
        if len(s) == 1 :
            
            return 1

        #set the max length 
        max_length = float("-inf")

        #make the ptrs 
        l = 0 

        #make the set 
        char_set = set()

        #make the loop over the array 
        for r in range(len(s)):

            while s[r] in char_set:

                char_set.remove(s[l])

                l += 1 

            char_set.add(s[r])

            max_length = max(max_length, r - l + 1)

        return max_length





s1 = "abcabcbb"

sol = Solution()

print(sol.lengthOfLongestSubstring(s1))