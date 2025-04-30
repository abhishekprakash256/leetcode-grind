"""
Given an integer array nums, reorder it such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

You may assume the input array always has a valid answer.
"""


"""
Example 1:

Input: nums = [3,5,2,1,6,4]
Output: [3,5,1,6,2,4]
Explanation: [1,6,2,5,3,4] is also accepted.

Example 2:

Input: nums = [6,6,5,6,3,8]
Output: [6,6,5,6,3,8]

 

Constraints:

    1 <= nums.length <= 5 * 104
    0 <= nums[i] <= 104
    It is guaranteed that there will be an answer for the given input nums.

 

Follow up: Could you solve the problem in O(n) time complexity?

"""



"""
approach -- 

do pass approach --

use first pass for the greater value alternatively

use the second pass for lower value checking 

for right to left 

to left to right 


0,1,2,3,4,5

[3,5,2,1,6,4]

[1,2,3,4,5,6]

[1,6,2,5,3,4]

brute force 
use n(logn)

better ? 

use two pointer 

[3,5,2,1,6,4]


"""



class Solution:
    """
    passes leetcode
    """
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        #constraint case 
        if len(nums) == 1 :

            return None

        #rearrange the array 
        for i in range(len(nums)-1) :

            if (i % 2 == 0 and nums[i] > nums[i+1]) or (i % 2 == 1 and nums[i] < nums[i+1]) :

                #swap the list
                nums[i] , nums[i+1] = nums[i+1] , nums[i]

        return None


















