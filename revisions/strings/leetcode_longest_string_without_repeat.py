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
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

"""
approach using sliding widnow 

max_
queue = [s[0]]

l = 0 
for r in range(1,len(s)) :
    
    while s[r] in queue and queue :

        queue.pop(0)

        l += 1 

    max_length = max(max_length , r - l + 1 )



        


"""


class Solution_slow():
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        The function to find the longest substring 
        """ 
        #constarint case 

        if not s :

            return 0

        if len(s) == 1 :

            return 1 

        #vars
        l , max_val = 0 , float("-inf")

        #make the queue 
        queue = [s[0]]

        #start the iter 
        for i in range(1,len(s)) :

            while s[i] in queue and queue :

                queue.pop(0)

                l += 1 

            max_val = max(i - l + 1 , max_val)
            
            queue.append(s[i])

        return max_val


class Solution():
    """
    passes leet code
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        The function to find the longest substring 
        """ 
        #constarint case 

        if not s :

            return 0

        if len(s) == 1 :

            return 1


        #make a char set 
        char_set = set()

        #vars 
        l , max_val = 0 , float("-inf") 

        for i in range(len(s)) :

            while s[i] in char_set :

                char_set.remove(s[l])

                l += 1

            char_set.add(s[i])

            max_val = max(i - l + 1 , max_val)

            

        return max_val
