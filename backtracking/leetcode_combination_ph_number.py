"""
Given a string containing digits from 2-9 inclusive, 
return all possible letter combinations that the number could represent. 
Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below.
 Note that 1 does not map to any letters.
"""

"""
Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:

Input: digits = ""
Output: []

Example 3:

Input: digits = "2"
Output: ["a","b","c"]

 

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].


"""



"""
approach -- 


# Define the mapping of digits to letters
mapping = {
'2': 'abc',
'3': 'def',
'4': 'ghi',
'5': 'jkl',
'6': 'mno',
'7': 'pqrs',
'8': 'tuv',
'9': 'wxyz'
}


using a helper dfs 

use backtracking 

idx pass and increase the idx + 1 

add the elemnt only if length is equal


"""

from typing import List


class Solution:
    def __init__(self):

        self.results = []

        self.mapper = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
            }

    def _helper_dfs(self,idx, combinations):
        """
        The funtion to make the combinations using backtracking
        """

        #base case

        #if the length if greater 
        if idx > len(self.digits) :

            return

        #if the combinatuion len is greater 
        if len(combinations) == len(self.digits) :

            self.results.append(combinations)

            return


        for char in self.mapper[self.digits[idx]] :

            self._helper_dfs(idx + 1 , combinations + char)




    def letterCombinations(self, digits: str) -> List[str]:
        """
        The function to find all the combinations of the letter 
        """
        self.digits = digits

        #constraiunt case 
        if not self.digits:

            return []

        #make the recursive calls
        self._helper_dfs(0,"")

        return self.results





















