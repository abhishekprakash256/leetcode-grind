"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and 
(i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""


"""

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1


"""


"""

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104


"""


"""
approach -- > 


use two pointer 

left and right 


left at 0 
right at len(height) - 1

area = min(right(height), left(height)) * ((right - left))





"""

from typing import List




class Solution:
	def maxArea(self, height: List[int]) -> int:
		"""
		The function to find the min max area between heights
		"""

		#constarint case
		if len(height) <= 1 :

			return 0

		#vars
		max_area , curr_area = 0, 0

		#ptrs
		l , r = 0 , len(height) - 1

		#start the loop
		while l < r :

			length = min(height[l] , height[r])

			width = r - l

			curr_area = length * width

			max_area = max( curr_area , max_area )

			if height[l] < height[r] :

				l += 1

			else:

				r -= 1

		return max_area





if __name__ == "__main__":

	height = [1,8,6,2,5,4,8,3,7]

	sol = Solution()

	res = sol.maxArea(height)

	print(res)