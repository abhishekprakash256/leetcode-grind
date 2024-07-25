"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false


"""


"""
1. brute force 

use a hash map of frequnecy table 
iterate all and compare and add to hash map 

do as that for second one too

matching both hashmap 
if freq matches then gives true 
else false 







"""



class Solution:
	def isAnagram(self, s: str, t: str) -> bool:
		"""
		The function to check for the anagram
		leetcode passed
		"""

		#make two hashmaps 
		mapper_one = {}
		mapper_two = {}


		#start the first loop for freq table 

		for i in s:

			if i in mapper_one :
				mapper_one[i] = mapper_one[i] + 1 

			else:
				mapper_one[i] = 1


		#start the first loop for freq table 

		for i in t:

			if i in mapper_two :
				mapper_two[i] = mapper_two[i] + 1 

			else:
				mapper_two[i] = 1



		#compare the hash map

		if mapper_one == mapper_two:
			return True

		else:
			return False















