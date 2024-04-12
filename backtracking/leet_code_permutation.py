"""

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""


"""
make the algo 

#vars 
def __init__(self):
    self.res = []
    self.mapper = {}


#base case 
if len(lst) == len(nums):
    res.append(lst)
    return 


two function structure 


def backtrack(self,lst)

    #base case 
    if len(lst) == len(nums):
        res.append(lst)
        return

    for i in self.nums:
        if i not in self.mapper:
            self.backttrack(lst.append(val))



def permute(self,nums)
    self.nums = nums
    for i in nums:
        mapper[i] = True
    
    self.backtrack([])

    return self.res


"""


class Solution():

    def __init__(self):
        self.res = []
        self.mapper = {}


    def bactrack(self,lst):
        """
        The backtrack helper function 
        """ 
        if len(lst) == len(self.nums):
            self.res.append(lst)
            return

        for i in self.nums:
            if i not in self.mapper:
                self.backttrack(lst.append(i))
        
        

    def permute(self,nums):
        """
        The main iter function 
        """
        self.nums = nums

        #make the hashmap
        for i in self.nums:
            self.mapper[i] = True

        self.bactrack(lst=[])

        return self.res