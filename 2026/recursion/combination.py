"""
basic template for the combinations
"""


res = []
path = []

nums = [1,2]

def dfs(i):

    if i == len(nums):
        res.append(path[:])
        return

    # take
    path.append(nums[i])
    dfs(i + 1)

    # undo
    path.pop()

    # skip
    dfs(i + 1)


dfs(0)

print(res)




class Solution():

    def __init__(self):

        self.path = []
        self.res  = []

    def dfs(self,i, nums):
        """
        The function to find the combinations
        """

        if i == len(nums): 

            self.res.append(self.path[:])
            return

        #take
        self.path.append(nums[i])
        self.dfs(i+1 , nums)

        # undo 
        self.path.pop()

        #skip
        self.dfs(i+1 , nums)



sol = Solution()


sol.dfs(0 , nums)

print(sol.res)