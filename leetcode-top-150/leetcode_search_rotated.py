"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k 
(1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1],
 nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] 
 might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it 
is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.


"""

"""
Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104

"""

"""
approch -- 


using a binary search 

basically using sorted array find the point where it can be 





"""

class Solution_wrong():

    def search(self,nums,target) :
        """
        The function to find the index of the target integer 
        """

        #constraints 
        if len(nums) == 1:

            if nums[0] == target :
                return 0
            else:
                return -1

        #make the ptrs 
        l , r = 0 , len(nums) - 1

        while l <= r :

            mid = (l + r) // 2

            if nums[mid] == target :
                return mid 
            
            elif nums[l] < target < nums[mid] : 

                r = mid - 1 

            elif nums[mid] < target < nums[r] :

                l = mid + 1

            elif nums[mid] > target and target < nums[r] :

                l = mid + 1 

            else :
                r = mid - 1 


        
        return -1



class Solution():

    def search(self,nums,target) :
        """
        The function to find the target elemnet in array 
        """

        #constraints 
        if len(nums) == 1:

            if nums[0] == target :
                return 0
            else:
                return -1

        #make the ptrs 
        l , r = 0 , len(nums) - 1

        while l <= r :

            mid = (l + r) // 2 

            if nums[mid] == target :
                return mid 

            if nums[l] <= nums[mid] :

                if nums[l] <= target <= nums[mid] :
                    r = mid -1 

                else:
                    l = mid + 1

            else:

                if nums[mid] <= target <= nums[r] :
                    l = mid + 1 
                else:
                    r = mid - 1

        return -1    