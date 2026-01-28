"""
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], 
return the minimum number of conference rooms required.

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

approach --> 

min = 0 

max = 30


The intution works as that we sort the array in the term of start and the end time of the meetingh

when start time is less end time we need a room 

when start time is greater than end time we don't need to increase the room 


we increase the room and keep a max counter for the room 







"""

from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        The function to find the meeting room required to do the meetings
        """

        #constaint case
        if len(intervals) <= 1 :

            return 1


        #list vars
        start_time = []

        end_time = []

        rooms = 0

        #loop and add in the list
        for start, end in zip(intervals) :

            start_time.append(start)

            end_time.append(end)

        #sort the lists
        start_time.sort()

        end_time.sort()

        #ptrs
        l , r = 0, 0

        #start the loop

        while (l + r) < 2*len(start) - 1 :

            if start_time[l] < end_time[r] :

                rooms += 1

                l += 1

            
            else :

                l += 1 

                r += 1


        return rooms




