"""
Given a string s, find the length of the longest without duplicate characters.

"""


"""
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

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
Approach --

res = 0 

edge case 

if len(s) == 0
	
	return s

two pointer approach -->

how do I check the repeat ? 

repeat can be in middle or anywher when adding ? 

start is imp either start , end , middle , at the ends

ends no

middle ? 

how to make desision of left and right expansion ? 

traverse from start ?? 

abcdbef

using a mapper with idx and then move the cursor 

keep the record of the length and updtae the max ?? 



"""


#not the correct solution right use sliding window with pooping the elements from the list structure

class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		"""
		The function to find the longest substring in the list
		"""

		#the res 
		res = 0

		#the edge condn
		if len(s) == 0:

			return s

		#make the storage dict
		mapper = {}

		#make the ptrs
		left = 0 
		right = left + 1

		#start the loop for traversal
		while left < right :

			mapper[s[left]] = True 

			if s[right] not in mapper :

				right += 1

				res = max(res, right - left + 1)

			else:

				mapper = {}


