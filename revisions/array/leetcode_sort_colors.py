"""
Given an array nums with n objects colored red, white, or blue, sort them in-place
 so that objects of the same color are adjacent, with the colors in the order red, white,
  and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue,
 respectively.

You must solve this problem without using the library's sort function.
"""


"""

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
 
"""

"""
approach -- 

imp parts -- 

only 3 colors 

sort in the place 

not use inbuild sorting function 

0,1,2

one pass algo no extra space 

0(n) time 

one pass use a one pointer to put all zeros in front 

[2,0,2,1,1,0]

[0,2,2,1,1,0]

[0,0,2,1,1,2]

[0,0,1,1,2,2]

"""

class Solution_wrong():

    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        #make the pointers of non zero element 
        l = 0 

        while l <= len(nums) - 1 :

            if nums[l] != 0 :

                break

            l += 1 

        #replace the zeros with one pass 
        for i in range(l,len(nums)):

            print(i)

            if nums[i] == 0 :

                nums[i] , nums[l] = nums[l] , nums[i]

                l +=1 

        #start from back and find the non 2 element 
        r = len(nums) - 1

        while r >= 0 :

            if nums[r] != 2 :

                break

            r -= 1

        #replace the 2 elemnets and make 2s
        for j in reversed(range(len(nums) , r)) :

            print(j)

            if nums[j] == 2 :

                nums[j] , nums[r] = nums[r] , nums[j]

                r -=1  



class Solution():
    def sortColors(self, nums) -> None:
        """
        Modify nums in-place to sort colors using two-pass swapping.
        """

        # Move all 0s to the beginning
        l = 0  # Pointer for placing 0s
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1

        # Move all 2s to the end
        r = len(nums) - 1  # Pointer for placing 2s
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] == 2:
                nums[j], nums[r] = nums[r], nums[j]
                r -= 1


sol = Solution()

test1 = [2,0,2,1,1,0]

print(sol.sortColors(test1))

print(test1)
