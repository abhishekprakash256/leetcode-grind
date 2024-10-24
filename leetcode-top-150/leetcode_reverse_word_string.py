"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

"""

"""
Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

"""

"""
constarints - 
	- remove spaces from left or right 
	- remove the multiple spaces 
	- keep single space only 

using O(1) space ? 

a revrse whole func
i =0 
j = len(s) - 1 

def rev(i,j):
	
	while i < j:

		s[i], s[j] = s[j], s[i]
		i += 1 
		j -= 1

"  hello world  "

"  world hello  "

leave only one space in betwenn and remove left and right space 

remove the right :

for i in strs:
    if i == " ":
        strs.replace()




"""


class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        left, right = 0, len(words) - 1

        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1

        return " ".join(words) 