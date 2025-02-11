"""
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number 
of intervals you need to remove to make the rest of the intervals non-overlapping.

Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] 
are non-overlapping.

"""

"""
Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

"""

"""
approach -- 


first sort the array 

[[1,2],[2,3],[3,4],[1,3]]

[[1,2],[1,3],[2,3],[3,4]]

intervals are now 

inervals[i][0] > intervals[i+1][0]

temp_int = intervals[i+1]

del result[i+1]

resullt.append(temp_int)

return result


[[1,2],[2,3],[3,4],[1,3]]



"""

from typing import List


class Solution:
    """
    passes leetcode 
    """
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        The function to remove the minimum number of overlapping intervals
        """

        # Edge case: If there's only one interval, no need for removal
        if len(intervals) <= 1:
            return 0

        # Sort intervals by end time to ensure we remove as few as possible
        intervals.sort(key=lambda i: i[1])

        # Variables
        i, result = 0, 0
        prev_end = intervals[0][1]  # Track end of last non-overlapping interval

        # Start the traversal from the second interval
        for j in range(1, len(intervals)):
            # If overlap occurs
            if intervals[j][0] < prev_end:
                result += 1  # Remove current interval
            else:
                prev_end = intervals[j][1]  # Update end of non-overlapping interval

        return result



nums= [[1,100],[11,22],[1,11],[2,12]]
sol = Solution()

print(sol.eraseOverlapIntervals(nums))


