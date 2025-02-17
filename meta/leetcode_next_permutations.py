"""
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

    For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].

The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

    For example, the next permutation of arr = [1,2,3] is [1,3,2].
    Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
    While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.

Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.
"""


"""
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]


Constraints:

    1 <= nums.length <= 100
    0 <= nums[i] <= 100

"""

"""
approach -- 

next grater after rearrangegment -- 
using the diguts given 

[1,2,3]


The replacement must be in place and use only constant extra memory. imp 





"""

from typing import List


class Solution_wrong:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        #constraint case 
        if len(nums) == 1 :

            return nums

        for i in range(len(nums) - 1 ,0, -1):

            #make the comparision

            if nums[i] > nums[i-1] and i-1 != 0 :

                #swap
                nums[i] , nums[i-1] = nums[i-1] , nums[i]

                return None

        #for whole case non decreasing
        l , r = 0 , len(nums) -  1

        #start the loop for swap
        while l <= r : 

            nums[l] , nums[r] = nums[r] , nums[l]

            l += 1 
            r -= 1 

        return None




class Solution:
    """
    passes leet code
    """
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Modifies nums in-place to the next lexicographical permutation.
        """

        n = len(nums)
        if n <= 1:
            return  # Edge case: single-element list

        # Step 1: Find first decreasing element from the right

        i = n - 2

        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:  # If such an element exists
            # Step 2: Find the next larger element to swap with
            j = n - 1
            while nums[j] <= nums[i]:  # Find the first larger element from the right
                j -= 1

            # Swap them
            nums[i], nums[j] = nums[j], nums[i]

        # Step 3: Reverse the elements after index `i`
        l, r = i + 1, n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
















