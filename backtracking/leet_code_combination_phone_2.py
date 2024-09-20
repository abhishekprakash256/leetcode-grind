"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""


"""
mapping string -

create a mapper = 
{2: "abc"  3: "def" , 4:"ghi" , 5:"jkl", 6:"mno" , 7:"pqrs", 8:"tuv", 9:"wxyz"}
"""

"""
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Input: digits = ""
Output: []


Input: digits = "2"
Output: ["a","b","c"]

"""


"""
bascially is a decision tree strcuture using recursion 

def __init__(self):
    self.mapper = {2: "abc"  3: "def" , 4:"ghi" , 5:"jkl", 6:"mno" , 7:"pqrs", 8:"tuv", 9:"wxyz"}
    self.res_lst = []

def helper(i,length,start_str):

    #base case
    if i == len(digits) - 1:
        self.res_lst.append(start_str)
    
    
    str_val = 

    strat_str =+ 
    
    for j in range(i,length):
        



def letterCombinations(self,digits: str):

    #make the base case 
    if len(digits) == 0 :
        return []

    #make the empty str 
    start_str = ""

    for i in len(digits):
        
        self.helper(i,digits[i] len(digits),start_str)
    
        
    return self.res_lst
        





"""
    

#-----------------------------------------------------------#-----------------------------------------------

class Solution():
    def __init__(self):
        self.mapper = { 2: "abc" ,3: "def" , 4:"ghi" , 5:"jkl", 6:"mno" , 7:"pqrs", 8:"tuv", 9:"wxyz"}
        self.res_lst = []
    

    def helper(self,idx,start_str,digits):
        """
        The helper dfs function
        """
        if len(start_str) == self.length:
            self.res_lst.append(start_str)
            return None

        
        current_digit = int(digits[idx])
        print(current_digit)
        

        for letter in self.mapper[current_digit]:
            
            self.helper(idx + 1, start_str + letter , digits)




    def letterCombinations(self,digits):
        """
        The main function
        passes leet code
        """
        #base case 
        if len(digits) == 0:
            return []

        self.length = len(digits)


        start_str = ""

        self.helper(0,start_str,digits)

        return self.res_lst



if __name__ == "__main__":
    sol = Solution()
    print(sol.letterCombinations("23"))
