"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product 
of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

"""

"""
Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


"""

"""
approach -- 

inp = [1,2,3,4] 

[1,2,6,24] front mul

[24,24,12,4] back mul 

out = [24,12,8,6]

"""

from typing import List

class Solution:
    """
    passes leetcode
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Make the product of the array except self 
        """

        #vars 
        forward_mul = []
        reverse_mul = []
        result = []

        mul = 1 
        
        #calc the foreard mul
        for i in nums :

            mul = i * mul

            forward_mul.append(mul)

        mul = 1 

        #calc the backaward mul
        for i in reversed(nums):

            mul = i * mul

            reverse_mul.append(mul)

        reverse_mul.reverse() #reverse the list again
       
        #make the list
        result.append(reverse_mul[1])

        i = 1 

        while i <= len(nums) - 2 :

            result.append(forward_mul[i-1] * reverse_mul[i+1])

            i +=1


        result.append(forward_mul[i-1])

        return result


sol = Solution()

print(sol.productExceptSelf([1,2,3,4] ))






