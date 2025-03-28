"""

You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are within the inclusive range.

A number x is considered missing if x is in the range [lower, upper] and x is not in nums.

Return the shortest sorted list of ranges that exactly covers all the missing numbers. That is, no element of nums is included in any of the ranges, and each missing number is covered by one of the ranges.



"""



"""

Input: nums = [0,1,3,50,75], lower = 0, upper = 99
Output: [[2,2],[4,49],[51,74],[76,99]]
Explanation: The ranges are:
[2,2]
[4,49]
[51,74]
[76,99]


Input: nums = [-1], lower = -1, upper = -1
Output: []
Explanation: There are no missing ranges since there are no missing numbers.


"""


"""
Ideas

1. Add the two start and the last value at the value on list

2. Use the two pointers, if the diffrence is less than one

"""




class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        missing_ranges = []

        last_seen = lower-1
        nums.append(upper+1)

        for i in range(len(nums)):
            if nums[i] - last_seen > 1:
                missing_ranges.append([last_seen+1, nums[i]-1])
            last_seen = nums[i]

        return missing_ranges
























































		
