"""
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
"""

"""
Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Example 3:

Input: nums = [0,1,1,1,1,1,0,0,0]
Output: 6
Explanation: [1,1,1,0,0,0] is the longest contiguous subarray with equal number of 0 and 1.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.

"""

from collections import Counter
from typing import List


class Solution_wrong():
    """
    sliding window doesn't work
    """

    def findMaxLength(self, nums: List[int]) -> int:
        """
        The function to find the max subarray of 1 and 0s 
        """

        #constarints 
        if len(nums) == 1 :

            return 0 

        #vars 
        nums_one = 0 
        nums_zero = 0
        results = float("-inf")


        #ptrs 
        l , r = 0 , 1

        if nums[l] == 0:

            nums_zero += 1 

        else:

            nums_one += 1

        while r <= len(nums) - 1 :

            #count the ones 
            if nums[r] == 1 :

                nums_one += 1

            else :

                nums_zero += 1

            #start to remove the left pointer 
            while nums_zero != nums_one :

                if nums[l] == 0 :

                    nums_zero -= 1 

                else :

                    nums_one -= 1 

                l += 1

            results = max(results, r - l + 1) 

            r += 1

        return results





class Solution():
    """
    passes leetcode
    """

    def findMaxLength(self, nums: List[int]) -> int:
        """
        The function to find the max subarray of 1 and 0s 
        """

        #constraint case 
        if len(nums) == 1 :

            return 0 

        #dict 
        mapper = {0: -1}  # Store first occurrence of each prefix sum
        
        #vars 
        prefix_sum = 0 
        max_length = 0


        #find the max length 
        for i, num in enumerate(nums):

            if num == 1 :

                prefix_sum += 1

            else :

                prefix_sum -= 1 

            if prefix_sum in mapper:
                
                max_length = max(max_length, i - mapper[prefix_sum])
            
            else:
                mapper[prefix_sum] = i  # Store first occurrence
        
        return max_length


 


