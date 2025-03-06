"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a 
space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

"""

"""
Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.


"""


"""
approach -- 

using a combination approach 

words can be used any number of times 

do a dfs and match the sequence length and if graeter doens't exists 

do a another router 

and can use a memoization for caching the results have true or false 

store a route in tuple ? with key as true and false

"""
from typing import List


class Solution_wrong:

    def __init__(self):

        self.memo = {}

    def helper_dfs(self,temp_combination):
        """
        The function to find the work combination exists
        """
        #print(temp_combination)

        #base case 
        if temp_combination == self.s:

                return True

        if temp_combination in self.memo:

            return self.memo[temp_combination]

        if len(temp_combination) > len(self.s):

            self.memo[temp_combination] = False

            return False

        for word in self.wordDict :

            if temp_combination not in self.memo

                if self.helper_dfs(temp_combination+word) :

                    self.memo[temp_combination] = True

                    return True
        
        return False



    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        The function to make the word break mactching 
        """

        self.s = s
        self.wordDict = wordDict

        temp_combination = ""

        return self.helper_dfs(temp_combination)



class Solution():
    """
    passes leetcode
    """

    def __init__(self):

        self.memo = {}

    def helper_dfs(self,start):
        """
        The helper dfs to find the word exists 
        """

        #base case 

        if start == len(self.s) :

            return True

        if start in self.memo :

            return self.memo[start]

        #do the dfs calls
        for word in self.wordDict :

            if self.s.startswith(word, start) :

                if self.helper_dfs(start + len(word)) :

                    self.memo[start] = True

                    return True

        self.memo[start] = False
        
        return False



    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        The funcrtion to find the word can be made from the word dict
        """

        self.s = s
        self.wordDict = set(wordDict) 

        return self.helper_dfs(0)












        
s = "leetcode"
wordDict = ["leet","code"]

sol = Solution()
print(sol.wordBreak(s,wordDict))


