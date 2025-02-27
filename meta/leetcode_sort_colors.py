"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, 
with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
"""


"""
Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]

 

Constraints:

    n == nums.length
    1 <= n <= 300
    nums[i] is either 0, 1, or 2.

 
"""

"""
approach -- 

when I see 2 I move to back 

one pass put all twos at back 

second pass put 0 at front 

use l and r pointer


"""


class Solution_wrong():
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        #costairnt case 
        if len(nums) == 1 :

            return None 


        #move the 2s 

        #ptrs
        l , r = 0, len(nums) - 1

        while l <= r :

            #find 2 and swap 

            if nums[l] == 2 :

                print("in")

                nums[l] , nums[r] = nums[r] , nums[l]

                r -= 1 

            l += 1


        #move the 0s 

        l , r = 0, 1

        while r <= len(nums) - 1  :

            #find the 0s 

            if nums[r] == 0 :

                nums[l] , nums[r] = nums[r] , nums[l]

                l += 1

            r += 1 


        return None


sol = Solution()


nums = [2,0,2,1,1,0]

print(sol.sortColors(nums))

print(nums)
