"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of 
characters. No two characters may map to the same character, but a character may map to itself.
"""



"""
Input: s = "egg", t = "add"

Output: true

Explanation:

The strings s and t can be made identical by:

Mapping 'e' to 'a'.
Mapping 'g' to 'd'.
Example 2:

Input: s = "foo", t = "bar"

Output: false

Explanation:

The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

Example 3:

Input: s = "paper", t = "title"

Output: true


"""



"""
things that are imp -- 

order and the freq 

s_mapper = {}
t_mapper = {}


for char in s:

	if char not in s_mapper :
		
		s_mapper[char] = 1
	
	else:
		
		s_mapper[char] = s_mapper[char] + 1

		
for char in t :

	if char not in t_mapper:
		
		t_mapper[char] = t_mapper[char] + 1

		

#match the mapper 

for char1,char2 in zip(s_mapper,t_mapper):

	if s_mapper[char1] != t_mapper[char2] :
		return False

return True
	


"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        passes leetcode 
        """
        if len(s) != len(t):
            return False

        s_to_t = {}
        t_to_s = {}

        for char_s, char_t in zip(s, t):
            # Check mapping from s to t
            if char_s in s_to_t:
                if s_to_t[char_s] != char_t:
                    return False
            else:
                s_to_t[char_s] = char_t

            # Check mapping from t to s
            if char_t in t_to_s:
                if t_to_s[char_t] != char_s:
                    return False
            else:
                t_to_s[char_t] = char_s

        return True

