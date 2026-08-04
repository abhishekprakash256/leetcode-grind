"""
basic template for the combinations ,where order don't matter
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
        self.res_lst = []


    def helper(self, start_lst, start):
        """
        The helper function
        """

        # base case
        if len(start_lst) == self.k:
            self.res_lst.append(start_lst)
            return


        for i in range(start, len(self.nums)):

            self.helper(start_lst + [self.nums[i]], i + 1)


    def combine(self, nums, k):
        """
        The main function
        """

        self.nums = nums
        self.res_lst = []

        self.helper([], 0)

        return self.res_lst



sol = Solution()


sol.dfs(0 , nums)

print(sol.res)