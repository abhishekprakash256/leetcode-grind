"""
Given a string s, remove duplicate letters so that every letter appears once and only once. 
You must make sure your result is among all possible results.
"""

"""

Example 1:

Input: s = "bcabc"
Output: "abc"

Example 2:

Input: s = "cbacdcbc"
Output: "acdb"

 

Constraints:

    1 <= s.length <= 104
    s consists of lowercase English letters.

 


"""


"""

approach -- 

sort 

start with 1st pos, check the last digit and remove the pos amd move 

the list will be short update the length 

"""


class Solution_wrong:

    def removeDuplicateLetters(self, s: str) -> str:
        """
        The function to remove the duplicate letters
        """

        #constraint case 
        #if length is 1 

        if len(s) == 1 :

            return s

        s_list = list(s)
        #sort the strings 

        s_list.sort()

        #get the length
        length = len(s_list)

        #ptrs 
        i = 1 

        while i < length :

            #find the equal val
            if s_list[i] == s_list[i-1] :

                del s_list[i]

            else :

                i += 1

            #update the length
            length = len(s_list)

        return ' '.join(s_list)
