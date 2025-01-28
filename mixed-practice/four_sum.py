"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a],
nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

"""

"""
Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]



we can sort : 

all have to be distinct 

[-2,-1,0,0,1,2]

make a recursion problem when add and also the sum is equal to target 

"""

class Solution_slow():

    def __init__(self):

        self.result = []

    def helper_dfs(self,i,temp_lst):
        """
        The helper function to find the target sum
        """


        #base case 

        #if sum is equal and 4 digits
        if len(temp_lst) == 4 and sum(temp_lst) == self.target :

            self.result.append(temp_lst)

            return

        #make the recursive call
        for j in range(i,len(self.nums)) :

            if j > i and self.nums[j] == self.nums[j - 1]:
               
                continue

            self.helper_dfs(j + 1 , temp_lst + [self.nums[j]] )
        



    def fourSum(self,nums, target):
        """
        The function to find the 4 sum of digits equal to target 
        """
        self.target = target
        self.nums = nums

        #sort the nums
        self.nums.sort()

        #make the vars 
        i = 0 
        temp_lst = []

        #make the recursive call
        self.helper_dfs(i,temp_lst)

        return self.result


