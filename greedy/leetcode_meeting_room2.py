"""
Given an array of meeting time intervals intervals 
where intervals[i] = [starti, endi], return the minimum number of conference rooms required.
"""


"""
Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1

 

Constraints:

1 <= intervals.length <= 104
0 <= starti < endi <= 106


"""


"""
approach --

min = 0 
max = 30

sort the array using the first val

meeting room we need is 1 

last max and next min 

room = 1 

max > min

    room += 1


rooms = [[9,10],[4,9],[4,17]]

sorted_rooms = [[4,9],[4,17],[9,10]] 

"""

from typing import List

class Solution_Wrong:
    """
    Wrong Solution
    """
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        The function to find the meeting rooms needed
        """

        #constraint case 
        if len(intervals) == 1:

            return 1

        #vars 
        room = 1

        #sort the list 
        intervals.sort() 

        #traverse the list 
        for i in range(1, len(intervals)) :

            if intervals[1][i-1] > intervals[i][0] :

                room += 1 

        return room




        