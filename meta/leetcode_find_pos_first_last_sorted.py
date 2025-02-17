"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending
 position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
"""


"""
Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109


"""

"""

approach -- 

using a normal binary 

search get the first and last point 

then run the custom binary search 

with edge case handling 

"""
from typing import List


class Solution_wrong:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        The search to find first and last of the occurance
        """

        #constrinats case 
        
        #if no nums
        if not nums :

            return [-1,-1]

        #if len of nums == 1
        if len(nums) == 1:

            return [0,0]

        #vars 
        result = [] 

        #ptrs 
        l , r = 0 , len(nums) - 1 
        idx_target = 0 
        first , last = 0 ,0 

        #start the search
        while l <= r :

            mid = (l + r) // 2 

            if nums[mid] == target :

                idx_target = mid

                #divinde into two parts and do search

                if idx_target != 0 :

                    #first part 
                    l1 , r1 = 0 , idx_target

                    while l1 <= r1 :

                        mid1 = (l1 + r1) // 2 

                        if nums[mid1] == target and nums[mid1 - 1] != target :

                            first = mid1

                        elif nums[mid1] <= target :

                            l1 = mid1 + 1 

                        else :

                            r1 = mid1 - 1

                else:

                    first = 0


                if idx_target != len(nums) - 1 :

                    #second part

                    l2 , r2 = idx_target , len(nums) - 1 


                    while l2 <= r2 :

                        mid2 = (l2 + r2) // 2 

                        if nums[mid2] == target and nums[mid2 + 1 ] != target :

                            last = mid2

                        elif nums[mid2] <= target :

                            l2 = mid2 + 1 

                        else :

                            r2 = mid2 - 1  

                else:

                    last = len(nums) - 1 


                return [first, last]


            elif nums[mid] < target :

                l = mid + 1 

            else :

                r = mid - 1

        return [-1,-1] #if any value is not found 




        

class Solution:
    """
    passes leetcode 
    """


    def binary_search_first(self,l,r) :
        """
        Do the fisrst binary seacrch
        """
        first = -1
        
        while l <= r :

            mid = ( l + r ) // 2

            if self.nums[mid] == self.target :

                first = mid
                r = mid - 1 

            elif self.nums[mid] < self.target :

                l = mid + 1 

            else :

                r = mid - 1 

        return first


    def binary_search_last(self,l,r) :
        """
        The function to find the last
        """

        last = -1

        while l <= r :

            mid = (l + r) // 2 

            if self.nums[mid] == self.target :

                last = mid
                l = mid + 1

            elif self.nums[mid] < self.target :

                l = mid + 1

            else :

                r = mid - 1 

        return last


    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Finds the first and last position of the target in a sorted array.
        """

        self.nums = nums 
        self.target = target

        #constarints case 
        
        #if no nums
        if not nums :

            return [-1,-1]

        #if len of nums == 1
        if len(nums) == 1:

            if nums[0] == target :

                return [0,0]

            else :

                return [-1,-1]

        #vars 
        result = []

        #ptrs
        l , r = 0 , len(self.nums) - 1 

        first = self.binary_search_first(l,r)
        last = self.binary_search_last(l,r)

        return [first, last]








