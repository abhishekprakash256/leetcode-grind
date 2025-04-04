"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

    0 <= a, b, c, d < n
    a, b, c, and d are distinct.
    nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.
"""



"""

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

 

Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109


"""


"""
approach -- 

use one pointer in start and travers the whole array 

Then 3 other points are needed 

recurison ? 

memo for faster approach ? 

tuple for memo 

decision tree but with memo faster ? 





"""


class Solution_wrong():

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        The function to find the four sum of the target sum that is given
        """

        #constraint case length is less
        if len(nums) <= 3 : 

            return -1

        #constarint case when length is equal
        if len(nums) == 4 :

            if sum(nums) == target  :

                return nums

        #vars 
        results = []

        #sort the array
        nums.sort()

        #start the traversal in both loops 
        for i in range(len(nums)):

            for j in range(i+1,len(nums)) :

                #start the binary search 

                #ptrs
                l = j + 1 
                r = len(nums) - 1 

                while l < r :

                    #sum
                    curr_sum = nums[i] + nums[j] + nums[l] + nums[r]

                    #mid
                    m = (l + r) // 2

                    #find the equal elemnents 
                    if i == j or i == r or l == r or j == r :

                        continue

                    elif curr_sum == target :

                        results.append([nums[i],nums[j],nums[l],nums[r]])

                    elif curr_sum > target :

                        r = m - 1

                    else :

                        l = m + 1

        return results



from typing import List


class Solution():
    """
    passes leetcode
    """

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        The function to find the four sum of the integer that is equal to target given
        """


        #constraint case length is less
        if len(nums) <= 3 : 

            return []

        #constarint case when length is equal
        if len(nums) == 4 :

            if sum(nums) == target  :

                return [nums]

        #vars 
        results = []

        #sort the array
        nums.sort()
        
        #length of nums
        length = len(nums) 

        for i in range(length - 3) :

            if i > 0 and nums[i] == nums[i-1]:

                continue

            for j in range(i+1,length - 2) :

                if j > i+1 and nums[j] == nums[j-1]:

                    continue
                #ptrs 
                l = j + 1 
                r = length - 1

                #start the binary search
                while l < r :

                    curr_sum = nums[i] + nums[j] + nums[l] + nums[r]

                    if curr_sum == target :

                        results.append([nums[i],nums[j],nums[l],nums[r]])

                        #skip the duplicates 
                        while l < r and nums[l] == nums[l+1]:

                            l += 1

                        while l < r and nums[r] == nums[r-1]:

                            r -= 1

                        l += 1
                        r -= 1

                    elif curr_sum < target :

                        l += 1 

                    else :

                        r -= 1

        return results










