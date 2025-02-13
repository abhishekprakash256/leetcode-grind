"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

"""

"""
Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

"""

"""

approach -- 

median odd -> then len(nums)//2 

median even -> then (len(nums) //2 , len(nums) //2 -1 ) / 2 

binary search ? 

brurte force 

will be array add 
then sort 

find median based on length 




"""


from typing import List

class Solution_brute_force():

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        The function to find the meadian of the array

        """

        #megee the array 
        nums1 = nums1 + nums2 

        #sort the array 
        nums1.sort()

        if len(nums1) % 2 == 0 :

            #even case 
            pos = (len(nums1) - 1) // 2 
            pos2 = ((len(nums1) -1 ) // 2) + 1

            return (nums1[pos] + nums1[pos2]) / 2

        else:

            #odd case 
            pos =  (len(nums1) - 1 ) // 2 

            return nums1[pos]



class Solution():

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        The function to find the meadian of the array

        """

        pass



