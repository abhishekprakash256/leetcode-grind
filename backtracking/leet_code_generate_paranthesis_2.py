"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

"""

"""
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]


Input: n = 1
Output: ["()"]

"""


"""
approach - 

left = 
right = 

#base case 
if n == 1:
    return ["()"]


def __init__(self):
    self.res_lst = []


def helper(self,start_str,left,right):

    #base case 
    if len(left + right) == n*2:
        return None
    
    
        #two cases
        if left < self.n:
            self.backtrack(s + "(",left + 1,right)
        
        if right < left:
            self.backtrack(s + ")",left, right + 1 )





        
    


  
def generateParenthesis(self,n):

    #base case 
    if n == 1:
        return ["()"]
    
    start_str = ""
    self.helper(start_str,0,0)

    return self.res_lst






"""

class Solution():

    def __init__(self):
        self.res_lst = []

    
    def helper(self,start_str,left,right):
        """
        The helper function to do the dfs
        """

        #constraint 
        if len(start_str) == 2*(self.n):
            self.res_lst.append(start_str)
            return None
        

        #left 
        if left < self.n:
            self.helper(start_str + "(", left + 1, right)
        
        if right < left:
            self.helper(start_str + ")", left , right + 1)
    

    def generateParenthesis(self,n):
        """
        The main function
        working in leetcode and passed test cases
        """
        self.n = n

        #base case 
        if n == 1 :
            return ["()"]
        
        start_str = ""

        self.helper(start_str, 0,0)

        return self.res_lst
