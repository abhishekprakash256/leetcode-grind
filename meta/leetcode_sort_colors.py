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

3 colors 

red, white and blue 

0 ,1, 2 

do in place 

first step

take all the zeros and pu in the same place 

second step 

take the 2s and put it in the last 

[1,2,1,0,0]



use two pinters side by side 

l , r = 0 , 0 

while r <= len(nums) - 1 :

    if nums[r] == 0 :

        nums[r] ,nums[l] = nums[l] , nums[r]

        l += 1 

    r += 1 


l , r = len(nums) - 1 , len(nums) - 1 

while l >= 0 :

    if nums[l] == 0 :

        nums[r] , nums[l] = nums[l] , nums[r]

        r -= 1 

    l -= 1 



[2,1,2]

"""


class Solution():
    """
    passes leetcode
    """
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        #constraint case 

        if len(nums) == 1 :

            return None

        #ptrs 
        l , r = 0 ,0 

        #swap the ones 
        while r <= len(nums) - 1 :

            #find the one val 
            if nums[r] == 0:

                nums[r] , nums[l] = nums[l] , nums[r]

                l += 1 

            r += 1 

        #ptrs 
        l , r = len(nums) - 1 , len(nums) - 1

        #swap the 2s 

        while l >= 0 :

            #find the 2 vals 
            if nums[l] == 2 :

                nums[r] , nums[l] = nums[l] , nums[r]

                r -= 1 

            l -= 1 

        return None

        






sol = Solution()


nums = [2,1,2]

print(sol.sortColors(nums))

print(nums)
