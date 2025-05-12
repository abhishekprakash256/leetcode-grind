"""
Given an array of integers nums and an integer limit, return the size of 
the longest non-empty subarray such that the absolute difference between any two 
elements of this subarray is less than or equal to limit.
"""

"""
Example 1:

Input: nums = [8,2,4,7], limit = 4
Output: 2 
Explanation: All subarrays are: 
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4. 
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4. 
Therefore, the size of the longest subarray is 2.

Example 2:

Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4 
Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.

Example 3:

Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3



Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
0 <= limit <= 109

"""



"""
approach -- 


use of the two pointer -- 

i , j 

max_val = float(-inf)
min_val = float(inf)
max_length = 0


if abs(max_val - min_val) <= limit :

    r += 1

while val > limit :
    
    update max 
    update min

    i += 1     
    

"""


class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        """
        The function to find the max array length with the limit value
        """

        #constraint case 
        if len(nums) == 1 :

            return 1

        #make the max and min value
        max_value = float("-inf")
        min_value = float("inf")

        #ptrs 
        l , r = 0 , 0

        #get the length 
        length = len(nums) - 1 

        #max length 
        max_length = 0

        #start the iter 
        while r <= length :

            max_value = max(max_value , nums[r])
            min_value = min(min_value , nums[r])

            diff = abs(max_value - min_value)

            #if the value if greater
            while diff > limit :

                l += 1 

                max_value = max_value (max_value , nums[l])
                min_value = min_value(max_value , nums[l])

                diff = abs(max_value - min_value)


            #chek if the diff get the condn
            if diff <= limit :

                max_length = max(max_length , r - l )

                r += 1 


        return max_length


            


        







































