"""
Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely
 of at least two shorter words (not necessarily distinct) in the given array.
"""

"""
Example 1:

Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
"dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".

Example 2:

Input: words = ["cat","dog","catdog"]
Output: ["catdog"]



Constraints:

1 <= words.length <= 104
1 <= words[i].length <= 30
words[i] consists of only lowercase English letters.
All the strings of words are unique.
1 <= sum(words[i].length) <= 105


"""



"""

approach -- 

use a dfs and make a set of the wordlist

check for prefix if martch continue and check if the word exists in the wordlist as well 

if exists add in the results

"""

from typing import List


class Solution_wrong:

    def __init__(self):
        self.results = []

    def _helper_dfs(self,temp_str):
        """
        The function to make the dfs calls for the tree
        """

        #print(temp_str)

        #base case 
        if temp_str != "" :

            if temp_str not in self.words :

                return

        #make the recursive calls 
        for word in self.words :

                temp_str += word

                if temp_str in self.words :

                    self.results.append(temp_str)

                #make the recusive call
                self._helper_dfs(temp_str)





    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        """
        Find the concateneeted words in the lists
        """

        self.words = set(words)

        #constarint case 
        if len(words) == 1 :

            return [words[0]]

        #make the function call
        temp_str = ""

        self._helper_dfs(temp_str)

        return self.results










from typing import List

class Solution:
    def __init__(self):
        self.words = set()
        self.memo = {}

    def _helper_dfs(self, word):
        """
        The function checks whether a word can be formed by concatenating other words.
        """
        if word in self.memo:
            return self.memo[word]

        for i in range(1, len(word)):  # Try splitting the word at different positions
            prefix = word[:i]
            suffix = word[i:]

            if prefix in self.words and (suffix in self.words or self._helper_dfs(suffix)):
                self.memo[word] = True
                return True
        
        self.memo[word] = False
        return False

    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        """
        Find all concatenated words in the given list.
        """
        # Store words in a set for O(1) lookup
        self.words = set(words)
        results = []

        # Check each word, but temporarily remove it from the set while checking
        for word in words:
            self.words.remove(word)  # Avoid self-comparison
            if self._helper_dfs(word):
                results.append(word)
            self.words.add(word)  # Restore the word in the set
        
        return results













class Solution():

    def __init__(self):

        self.memo = {}


    def _helper_dfs(self, word):
        """
        The funciton to find the words in the list by dfs
        """

        #base case 
        if word in self.memo :

            return self.memo[word]

        #make the recursive calls 
        for i in range(1,len(word)) :

            prefix = word[:i]
            suffix = word[i:]

            if prefix in self.words and (suffix in self.words or self._helper_dfs(suffix)) :

                self.memo[word] = True

                return True

        
        self.memo[word] = False

        return False     



    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        """
        The function to find the concatenated strings in word list
        """

        self.words = set(words)



        #constraint case 
        if len(self.words) == 1:

            return []

        results = [] 

        #make the recursive calls
        for word in self.words :

            self.words.remove(word)

            if self._helper_dfs(word) :

                results.append(word)

            self.words.add(word)


        return results













words = ["cat","dog","catdog"]

words2 = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]


sol = Solution()

print(sol.findAllConcatenatedWordsInADict(words2))


















