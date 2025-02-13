"""
Given an integer array nums, return all the triplets [nums[i], nums[j],
 nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] = 0.

Notice that the solution set must not contain duplicate triplets.
"""


"""

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.



"""

"""
approach -- 

use one pointer and two pointer inside

move per mid value using binary search -- 

"""
from typing import List

class Solution_wrong:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        The function to form the tiplet that can form the sum
        """

        #constarint case 
        if sum(nums) == 0 and len(nums) == 3 :

            return [nums]

        #sort the array 
        nums.sort()

        #make the result list 
        result = []
        
        #start the loop
        for i in range(len(nums)-2) :

            #ptrs
            l , r = i + 1 , len(nums) - 1

            while l < r :

                print(l,r)

                mid = (l + r) // 2

                temp_sum = nums[i] + nums[l] + nums[r]   

                if temp_sum == 0 and i != l and i != r and l != r :

                    result.append([nums[i],nums[l],nums[r]])

                elif temp_sum > 0 :

                    r = mid - 1

                else :

                    l = mid + 1

        return result






class Solution():
    """
    passess leetcode 
    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        The function to form the tiplet that can form the sum
        """

        #constarint case 
        if sum(nums) == 0 and len(nums) == 3 :

            return [nums]

        #sort the array 
        nums.sort()

        #make the result list 
        result = []

        #start the loop 
        for i in range(len(nums)-2):

            if i > 0 and nums[i] == nums[i-1] :

                continue

            #ptrs
            l , r = i + 1 , len(nums) - 1 

            while l < r :

                temp_sum = nums[i] + nums[l] + nums[r] 

                if temp_sum == 0 :

                    result.append([nums[i],nums[l],nums[r]])

                    #skip the duplicates
                    while l < r and nums[l] == nums[l+1] :

                        l += 1

                    while l < r and nums[r] == nums[r-1]:

                        r -= 1

                    l +=1 
                    r -=1 

                elif temp_sum > 0 :

                    r -= 1 

                else :

                    l += 1

        return result 

















nums = [-1,0,1,2,-1,-4]

sol = Solution()

print(sol.threeSum(nums))