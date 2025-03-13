"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.
"""

"""
Example 1:

Input: nums = [1,1,1], k = 2
Output: 2

Example 2:

Input: nums = [1,2,3], k = 3
Output: 2



Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107


"""

"""
sliding window ? 

when sum is less add when greter slide the left pointer 

and increase the counter for subarray 

"""

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        #constraints 

        if len(nums) == 1 :

            if nums[0] == k :

                return 1 

            else :

                return -1

        #ptrs 
        l = 0 

        count = 0 #array counter 

        run_sum = nums[0] #running sum

        #start the loop 
        for i in range(1,len(nums)) :

            if run_sum == k :

                count += 1 

            run_sum += nums[i]

            while run_sum > k :

                run_sum -= nums[l]

                l += 1

        return count




        
