"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 
"""


"""
Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]

 

Constraints:

1 <= n <= 8

"""



"""
approach -- 

using dfs 

and helper method

make a valid paranthesis ensuring open and close 

make left and right equal somethow




"""

class Solution:

    def __init__(self):

        self.results = [] 

    def _helper_dfs(self,combinations, left , right):
        """
        The function to make the paranthesis
        """
        
        #base case 
        if len(combinations) == 2 * (self.n)  :

            self.results.append(combinations)

            return

        #make the combinations recurive calls


        if left < self.n :

            self._helper_dfs(combinations + "(", left + 1 , right)

        if right < left :

            self._helper_dfs(combinations + ")", left, right + 1 )





    def generateParenthesis(self, n: int) -> List[str]:
        """
        The function to make the paranthesis
        """

        self.n = n 

        #constraint case 
        if self.n == 1 :

            return ["()"]

        #make the recursive calls
        self._helper_dfs("",0,0)

        #return the results
        return self.results







