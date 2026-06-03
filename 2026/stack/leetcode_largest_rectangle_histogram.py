"""

Given an array of integers heights representing the histogram's bar 
height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
"""

"""

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
"""



"""

approach -- 

using two pointer -- 

height is the min of between the two 

width = r - l + 1 

move the ptr based on which is small 

store max and curr area 

"""

from typing import List



class Solution():
	def largestRectangleArea(self, heights: List[int]) -> int:
		"""
		The function to find the max area of rect
		This is not possible as the rectangle has to be vertical not horizontal
		"""

		if len(heights) == 1 :

			return heights[0]

		#result
		res = 0 

		#currrent area 
		curr_area = 0

		#ptrs 
		l , r = 0 , len(heights) - 1  

		#start the loop
		while l < r :

			if ( (r - l) + 1) <= min(heights[l] , heights[r] ) :

				curr_area = min(heights[l] , heights[r] ) * (r - l + 1)

				res = max(curr_area , res)

			if heights[l] > heights[r] :

				r -= 1 


			else :

				l += 1

			#print(curr_area)


		return res


sol = Solution()

heights = [2,1,5,6,2,3]

res = sol.largestRectangleArea(heights)

print(res)