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
Constraints:

	0 <= s.length <= 5 * 104
	s consists of English letters, digits, symbols and spaces.

"""


"""
approach --- 

using a set to track the values 
and a var to store the max length 

pop the values using while loop 



str_len = 0
mapper = set()
left = 0


for right in range(len(s)) :

	mapper.add(s[right])

	res = max(right - left + 1 , res)

	while s[right] in mapper :

		left += 1 

		mapper.remove(s[left])

return res


"""


class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		"""
		The function to find the longest substring array
		optimal soln
		"""
		
		#edge case 
		if len(s) == 0 :

			return 0 

		if len(s) == 1 :

			return 1

		#res var 
		str_len = 0

		#set for unique strings
		str_set = set()

		left = 0

		#start the traversal 
		for right in range(len(s)) :

			while s[right] in str_set :

				str_set.remove(s[left])

				left += 1


			str_set.add(s[right])

			str_len = max(right - left + 1  , str_len)


		return str_len


test = "abcabcbb"

test2 ="bbbbb"

test3 = "pwwkew"

sol = Solution()

res = sol.lengthOfLongestSubstring(test3)


print(res)

