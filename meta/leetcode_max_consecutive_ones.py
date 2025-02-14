"""
Given a binary array nums and an integer k, return the maximum 
number of consecutive 1's in the array if you can flip at most k 0's.
"""


"""
Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length

"""

"""
approach -- 

using a sliding wirndow approach -- 


smaller the window as zeros more than k 

"""

from typing import List

class Solution_wrong():

    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        The function to find the largest consecutive ones
        """
        #constraints case 
        if len(nums) == 1 :

            if nums[0] == 1 :

                return 1

            else :

                if k == 1:

                    return 1 

                else :

                    return 0   

        #vars 
        l , curr , max_length = 0 , 0 , float("-inf")

        for i in range(len(nums)):

            if nums[i] == 0 :

                curr +=1
            
            while curr > k :

                if nums[l] == 0 :

                    curr -= 1 
                    l +=1 

            curr = 0

            max_length = max(max_length , i - l + 1)

        return max_length







        