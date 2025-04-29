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



class Solution_Wrong():
    """
    Wrong Solution
    """
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        The function to find the meeting rooms needed
        """

        #constarint case 
        if len(intervals) == 1 :

            return 


        #the list
        start_lst = []
        end_lst = []

        #vars
        count = 0 
        res = 0
        i = 0


        #iter the list and append the values
        for start, end in intervals :

            start_lst.append(start)
            end_lst.append(end)

        #sort the list
        start_lst.sort()
        end_lst.sort()

        #compare the time 
        while i < len(intervals) :

            if start_lst[i] < end_lst[i] :

                count += 1

            else :

                count -= 1


            res = max(count, res)
            i += 1

        return res

        



class Solution():
    """
    passes leetcode
    """

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        The function to find the meeting roorm rquired
        """

        #constraint case
        if len(intervals) == 1 :

            return 1

        #make the list 
        start_lst = []
        end_lst = []

        #apend in the list
        for start, end in intervals :

            start_lst.append(start)
            end_lst.append(end)

        #sort the array
        start_lst.sort()
        end_lst.sort()

        #make the ptrs
        s , e = 0 , 0 
        count , res = 0 , 0  

        #iter the values
        while s < len(intervals) :

            if start_lst[s] < end_lst[e] :

                s += 1
                count += 1 

            else :

                e += 1
                count -= 1

            res = max(res, count)

        return res
                