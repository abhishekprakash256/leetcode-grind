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

from collections import defaultdict

class Solution():
    """
    The function to find the sum 
    """

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

                return 0


        #vars 
        prefix_sum = 0 
        mapper = defaultdict(int)
        mapper[0] = 1  
        count = 0 

        for num in nums :

            prefix_sum += num

            if (prefix_sum - k) in mapper :

                count += mapper[prefix_sum - k]

            mapper[prefix_sum] += 1 


        return count









        
