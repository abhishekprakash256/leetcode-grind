"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, 
starting with word1. If a string is longer than the other, append the additional letters onto the end 
of the merged string.

Return the merged string.



"""

"""

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s

Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d



1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.


"""

"""
approach- 

using two pinters 

l,r = 0,0 


while l <= len(s1) -1 or r <= len(s2) - 1 :

	combined += s1[l]
	combiner += s2[r]

	l += 1 
	r += 1

while  :

	combined += s[]

"""


class Solution():

	def mergeAlternately(self, word1: str, word2: str) -> str:
		"""
		The function to merge two words 
		passes leetcode
		"""

		length1 = len(word1) - 1 
		length2 = len(word2) - 1 


		#make the ptr 
		l , r = 0 ,0 

		#make the combined string
		combined_str = ""

		#combine alterbatively
		while l <= length1 and r <= length2 :

			combined_str += word1[l]
			combined_str += word2[r]

			l += 1 
			r += 1 


		#combine the remaining
		while l <= length1:

			combined_str += word1[l]

			l +=1 

		while r <= length2:

			combined_str += word2[r]

			r +=1 


		return combined_str 












