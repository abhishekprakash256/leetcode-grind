"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

"""

"""
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9


n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105


"""


"""
approach -- 

two pointer system 

starts with l and r at 0 , 1 pos 

move with while loop --

if nums[r] <= nums[l] :

    height1 = max(nums[r],nums[l])
    height2 = min(nums[r],nums[l])

    curr_area = abs(height1 - height2) * 1 

area += curr_area


"""


class Solution_wrong():

    def trap(self, height) -> int:
        """
        The function to find the trap water in heights array
        """

        #constraints case
        if len(height) == 1 :

            return 0

        #make the vars
        area = 0
        curr_area = 0 

        #pointers
        l , r = 0 , 1 

        while r <= len(height) - 1 :

            if height[l] > height[r] :

                curr_area +=  abs(max(height[r] , height[l]) - min(height[r], height[l] ) )  #get the curr area
            
            else:

                area += curr_area #update the max area 

                l = r

            r += 1

        return area 



class Solution:

    def trap(self, height: list[int]) -> int:
        if not height or len(height) < 3:
            return 0  # No water can be trapped if there are less than 3 bars.

        # Initialize pointers and variables
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        water_trapped = 0

        # Use two pointers to traverse the array
        while left < right:
            if height[left] < height[right]:
                # Process the left pointer
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water_trapped += left_max - height[left]
                left += 1
            else:
                # Process the right pointer
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water_trapped += right_max - height[right]
                right -= 1

        return water_trapped







test1 = [4,3,2,3]

sol = Solution()

print(sol.trap(test1))


