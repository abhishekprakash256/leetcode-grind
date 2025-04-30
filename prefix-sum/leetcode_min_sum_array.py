"""
Given an array of positive integers nums and a positive integer target, 
return the minimal length of a whose sum is greater than or equal to target.
If there is no such subarray, return 0 instead.
"""


"""
Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0


Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104

 
Follow up: If you have figured out the O(n) solution, 
try coding another solution of which the time complexity is O(n log(n)).


"""


"""
approach -- 

prefix_sum = add the value when value is greater or equal we get the length 

when the value is less we add the  value

we subtract the left value and add the right value

move the pointer accordingly 


"""

from typing import List

class Solution_Wrong():

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        The function to find the min sub array whose sum matches or greater
        """

        #constraint case 
        if len(nums) == 1 :

            if nums[0] >= target :

                return 1

            else :

                return 0

        #vars
        prefix_sum = 0
        l , r = 0 ,0 
        length = len(nums)
        min_len = float("inf")


        #iterate the array
        while r <= length - 1 :

            #print(prefix_sum)

            if prefix_sum  < target :

                prefix_sum += nums[r]
                
                r += 1


            else :

                min_len = min(r - l , min_len)

                prefix_sum -= nums[l]

                l += 1 

            print(l,r)

        if not min_len :

            return 0 

        return min_len






class Solution():
    """
    passese leetcode
    """

    def minSubArrayLen(self,target , nums) :
        """
        The function to find the min sum  array
        """

        #constraint case 

        if len(nums) == 1 :

            if nums[0] >= target :

                return 1

            else :

                return 0

        #vars
        l  = 0 
        prefix_sum = 0 
        min_len = float("inf")


        for i in range(len(nums)) :

            prefix_sum += nums[i]

            while prefix_sum >= target :

                min_len = min(i - l +1 , min_len)

                prefix_sum -= nums[l]

                l += 1 

        return 0 if min_len == float("inf") else min_len




target = 7
nums = [2,3,1,2,4,3]



sol = Solution()

res = sol.minSubArrayLen(target, nums)

print(res)














