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

nums = [1,2,3]



class Solution():

    def __init__(self):
        self.res = []


    def backtrack(self,lst):
        """
        The backtrack helper function 
        """ 
        if len(lst) == len(self.nums):
            self.res.append(lst)
            return

        for i in self.nums:

            if i not in lst:
                
                self.backtrack(lst + [i])


    def permute(self,nums):
        """
        The main iter function 
        """
        self.nums = nums

        #make the hashmap

        self.backtrack([])

        return self.res









"""

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""



class Solution:
    """
    passees leetcode
    """
    def __init__(self):

        self.results = []

    def _helper_dfs(self,permutations) :
        """
        The function to make the dfs calls for permutations
        """

        #base case 
        if len(permutations) == len(self.nums) :

            self.results.append(permutations[:])

            return

        #make the recursion calls
        for i in range(len(self.nums)):

            #check if the value is there
            if self.nums[i] in set(permutations):

                continue

            #add the value 
            permutations.append(self.nums[i])

            #recusive calls
            self._helper_dfs(permutations)

            permutations.pop()



    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        The function to find all the possible permutations 
        """

        self.nums = nums 

        #constraint case 
        if len(self.nums) == 1 :

            return [self.nums]

        #vars
        permutations = []

        #make the recursion calls 
        self._helper_dfs(permutations)

        #return the results
        return self.results










        
























if __name__ == "__main__":
    sol = Solution()
    print(sol.permute(nums))

