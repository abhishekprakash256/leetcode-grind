"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
"""


"""
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]



"""

"""

brute force soln  -- 


pop and add approach in the array 

like pop and add on top of the array using the loop

use the extra space and o(n)


optimal approach --- 

[1,2,3,4,5,6,7]

[5,6,7,1,2,3,4]

[4,3,2,1,7,6,5] rotation 

[5,6,7,1,2,3,4] replace 


if k > len(nums):
	k = len(nums) - k


"""


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Leetcode passed optimal approach 
        """

        #base case 
        if len(nums) == 1 :
            return nums
        
        #make the ptr 
        if k > len(nums):
            res = k - len(nums)
            k = len(nums) - res
        
        else:
            k = len(nums) - k 
        
        #make the replace 
        def replace(i,r):

            #start the loop 
            while i < r:
                nums[i],nums[r] = nums[r], nums[i]
                i += 1
                r -= 1
        
        replace(0,k-1)
        replace(k,len(nums)-1)
        replace(0,len(nums)-1)

        return nums

    
        

        

