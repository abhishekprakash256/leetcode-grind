"""
A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.

For example, a string such as "substitution" could be abbreviated as (but not limited to):


For example, a string such as "substitution" could be abbreviated as (but not limited to):

	"s10n" ("s ubstitutio n")
	"sub4u4" ("sub stit u tion")
	"12" ("substitution")
	"su3i1u2on" ("su bst i t u ti on")
	"substitution" (no substrings replaced)

The following are not valid abbreviations:

	"s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
	"s010n" (has leading zeros)
	"s0ubstitution" (replaces an empty substring)

Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

A substring is a contiguous non-empty sequence of characters within a string.

Constraints:

	1 <= word.length <= 20
	word consists of only lowercase English letters.
	1 <= abbr.length <= 10
	abbr consists of lowercase English letters and digits.
	All the integers in abbr will fit in a 32-bit integer.

"""


"""

Example 1:

Input: word = "internationalization", abbr = "i12iz4n"
Output: true
Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n").

Example 2:

Input: word = "apple", abbr = "a2e"
Output: false
Explanation: The word "apple" cannot be abbreviated as "a2e".

"""








"""

approach ---> 

two pointer and check for the digit 
and skip if the value is 0 

word = apple 
abbr = a2e 


two pointer at word and abbr 

start at 0

l, r = 0,0

check for is digit and make a Tens 

if abbr[r].isdigit() :

	if abbr[r+1].isdigit() :

		traverse = abbr[r] * 10 + abbr[r+1]

		r += 1 

	else :

		traverse = abbr[r]

	l += traverse 



if abbr[r] != word[l] :

	return false 


return True 














"""




class Solution:
	def validWordAbbreviation(self, word: str, abbr: str) -> bool:
		"""
		The function to find the abbr and word match
		!!! NOT WORKING !!!
		"""

		#make the ptrs 
		l, r = 0, 0


		while l < len(abbr) :


			if abbr[l].isdigit():

				if int(abbr[l]) == 0:

					return False

				elif abbr[l+1].isdigit() :

					travserse = int(abbr[l]) * 10 + int(abbr[l])

					l += 2 

					r = travserse

				else :

					travserse = int(abbr[l])

					l += 1 

					r = travserse


			print(abbr[l] , l)

			print(word[r] , r)

			if abbr[l] != word[r] :

				return False

			l += 1
			r += 1

			travserse = 0 


		return True






word = "internationalization"

abbr = "i12iz4n"


sol = Solution()


res = sol.validWordAbbreviation(word , abbr)


print(res)