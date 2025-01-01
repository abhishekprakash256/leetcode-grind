"""
Given an array of integers nums sorted in non-decreasing order, find the starting and 
ending position of a given target value.

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


using binary search

and linear for boundary and get the first and last 

set the first and last as -1,-1

and use two loops to iter the boundaries

"""


from typing import List

class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        The function to find the start and end indices of a target value in a sorted array.
        """
        # Constraints
        if not nums:
            return [-1, -1]

        # Initialize pointers
        l, r = 0, len(nums) - 1

        # Initialize boundaries
        first, second = -1, -1

        # Start binary search
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                # Traverse left to find the first occurrence
                first = mid
                while first > 0 and nums[first - 1] == target:
                    first -= 1

                # Traverse right to find the second occurrence
                second = mid
                while second < len(nums) - 1 and nums[second + 1] == target:
                    second += 1

                break  # Found the target range; exit the loop

            elif nums[mid] < target:
                l = mid + 1

            else:
                r = mid - 1

        return [first, second]



