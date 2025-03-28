"""
There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose 
horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. 
There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

 
"""


"""

Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].

Example 2:

Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.

Example 3:

Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
- Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].


"""



"""

#base case 
if len(nums) == 1:
	return 1



#vars 
count = 1

i = 1 


#sort the array


while i < len(points):


	temp_val = points[i-1][1]


	if points[i-1] <= temp_val <= points[i][1] :

		count +=1
		i += 2

	else:

		count += 1

		i +=1



"""


from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        Function to find the minimum number of arrows needed to burst all balloons.
        """

        # Base case: if there's only one balloon, we need one arrow
        if len(points) <= 1:
            return len(points)

        # Sort balloons by their end coordinates
        points.sort(key=lambda x: x[1])

        # Initialize the count and the position of the first arrow
        count = 1
        arrow_position = points[0][1]

        # Loop through each balloon interval
        for i in range(1, len(points)):
            # If the start of the current balloon is beyond the position of the last arrow
            if points[i][0] > arrow_position:
                # We need a new arrow for this balloon
                count += 1
                # Update the arrow position to the end of the current balloon
                arrow_position = points[i][1]

        return count











