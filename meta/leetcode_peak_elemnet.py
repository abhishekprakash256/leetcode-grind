"""
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.
"""

"""


Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
 

Constraints:

1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.
"""

"""

approach -- 

using binary search 

#case all are equal 
[1,1,1]

if m-1 < 0:

    if nums[m] > nums[m+1] :
        
        return m

if m+1 > len(nums) -1 :

    if nums[m-1] < nums[m] :

        return m

if nums[m-1] < nums[m] and nums[m] > nums[m + 1 ]:

    return m


"""


class Solution_wrong:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        wrong soln
        The funtion to find the peak elemnet in the array 
        """
        #constraint case 
        if len(nums) == 1 :

            return nums[0]


        #make the ptrs 
        l , r  = 0 , len(nums) - 1 

        #start the element finding 
        while l < r :

            m = ( l + r) // 2

            #case of first element :
            if m-1 < 0:

                if nums[m] >= nums[m+1] :
                    
                    return m

            if m + 1 > len(nums) - 1 :

                if nums[m-1] <= nums[m] :

                    return m 

            if nums[m-1] < nums[m] and nums[m] > nums[m+1] :

                return m 


            elif nums[m] < nums[m + 1 ] :

                r = m - 1 

            else :

                l = m + 1 

        return r 





"""
approch -- 
given out the index of the array 

[1,2,1] -> 1 

[2,3,1,4] -> 3 

[1,2,3,4] -> 4 

binary search --> 

if nums[m-1] < nums[m] and nums[m] > nums[m+1] : 

    return m 

elif l == m and nums[m] > nums[m+1] :

    return l 

elif r == m and nums[m-1] < nums[m] :

    return r 

else : 

    r = m - 1 


"""










from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        Find a peak element using binary search.
        """

        # Base case: If there's only one element, return index 0
        if len(nums) == 1:
            return 0

        # Binary Search Initialization
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2

            # If nums[m] < nums[m+1], move to the right half (possible peak exists)
            if nums[m] < nums[m + 1]:
                l = m + 1
            else:  # Otherwise, move to the left half
                r = m 

        return l  # l and r will converge to the peak index


















































