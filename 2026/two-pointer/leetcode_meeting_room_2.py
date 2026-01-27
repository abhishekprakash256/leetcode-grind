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