"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Input: n = 1
Output: ["()"]


"""

class Solution():
    def __init__(self):
        self.res = []

    def backtrack(self,s, left,right):
        """
        The funciton to make the paranthesis
        """
        #base case 
        if len(s) == 2 *self.n:
            self.res.append(s)
            return
        
        #two cases
        if left < self.n:
            self.backtrack(s + "(",left + 1,right)
        
        if right < left:
            self.backtrack(s + ")",left, right + 1 )
        



    def generateParenthesis(self,n):
        self.n = n 
        """
        The funciton to generate the paranthesis 
        """
        
        self.backtrack("",0,0)

        return self.res

