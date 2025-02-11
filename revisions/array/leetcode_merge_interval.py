"""
Given an array of intervals where intervals[i] = [starti, endi], merge all 
overlapping intervals, and return an array of the non-overlapping intervals 
that cover all the intervals in the input.
"""

"""
Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

[[1,3],[2,6],[8,10],[15,18]]

[[1,3],[2,6],[5,10],[15,18]]

[[1,3],[4,6],[5,10],[15,18]

"""


"""
approach -- 

compare the first[last], second[first]

if first[last] >= second[first]

else :

    i += 1

we can use a while loop and compare and traverse the i 


[[1,3],[2,6],[8,10],[15,18]]
"""

class Solution:
    """
    passes leetcode but slow 
    """

    def merge(self, intervals):
        """
        The function to merge the intervals 
        """

        #constarints case 

        if len(intervals) == 1:

            return [intervals[0]]


        #sort the list 
        intervals.sort( key = lambda i : i[0] )

        #vars 
        i = 0

        #start the interation
        while i <= len(intervals) - 2 :

            #case where intervals merge 
            if intervals[i][1] >= intervals[i+1][0] :

                min_val = min(intervals[i][0], intervals[i+1][0])
                max_val = max(intervals[i][1] , intervals[i+1][1])

                del intervals[i+1]

                intervals[i][0] = min_val
                intervals[i][1] = max_val

            else:

                i +=1

        return intervals



       










