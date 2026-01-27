"""

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

"""

"""

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9



"""



"""


Constraints:

	n == height.length
	1 <= n <= 2 * 104
	0 <= height[i] <= 105

"""


"""

how we trap water ? 

we need to know diff of the length and trap water 

left and right pointer 

we move left and right 


if right is less than left we move right 

always the water depends on height diff , that works with staright void case but not with vars ones ? 

we set two pointers on the diff place where the diff is less and then find the area  ? 

if right +1 > right then we stop the movement 

left stays on the place now move the and calc the water ? 

left stops where left > left + 1

then move left and calc based on the (left - curr) height * 1 

add up into the last to sum up 



how about we move them from start to end ? 

not gonna work

https://www.hellointerview.com/learn/code/two-pointers/trapping-rain-water




"""

"""
approach ---> 


max_left = height[0]

max_right = height[len(height) - 1]

height[left] <= max_left 

trap+= 1 

height[right] >= max_right 

trap += 1 

if max_left > max_right :




"""













from typing import List



class Solution:

    def trap(self, height: List[int]) -> int:

        if len(height) < 3:
            return 0

        l, r = 0, len(height) - 1

        max_left, max_right = 0, 0

        trap_water = 0

        while l < r:

            if height[l] < height[r]:

                if height[l] >= max_left:

                    max_left = height[l]

                else:
                    trap_water += max_left - height[l]

                l += 1

            else:

                if height[r] >= max_right:

                    max_right = height[r]

                else:

                    trap_water += max_right - height[r]

                r -= 1

        return trap_water




height = [0,1,0,2,1,0,1,3,2,1,2,1]


sol = Solution()


print(sol.trap(height))































