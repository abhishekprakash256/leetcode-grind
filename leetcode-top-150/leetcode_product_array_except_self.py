"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""

"""
Input: nums = [1,2,3,4]
Output: [24,12,8,6]


Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

"""


"""
prefix = [1,2,6,12]

postfix = [24,24,12,4]

output = [24,12,8,6]


how to make the output array -- 


out = [postfix[1],prefix[0]*postfix[2],prefix[1]*postfix[len(postfix)-1],prefix[len(prefix)-2]]
"""