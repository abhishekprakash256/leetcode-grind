"""
You are given a 0-indexed integer array nums, where nums[i] is a digit between 0 and 9 (inclusive).

The triangular sum of nums is the value of the only element present in nums after the following process terminates:

Let nums comprise of n elements. If n == 1, end the process. Otherwise, create a new 0-indexed integer array newNums of length n - 1.
For each index i, where 0 <= i < n - 1, assign the value of newNums[i] as (nums[i] + nums[i+1]) % 10, 
where % denotes modulo operator.
Replace the array nums with newNums.
Repeat the entire process starting from step 1.
Return the triangular sum of nums.
"""


"""

Input: nums = [1,2,3,4,5]
Output: 8
Explanation:
The above diagram depicts the process from which we obtain the triangular sum of the array.
Example 2:

Input: nums = [5]
Output: 5
Explanation:
Since there is only one element in nums, the triangular sum is the value of that element itself.
 
"""



"""
approach -- 

length = len(nums)

while length != 1 

    for i in (1,length) :

        new_lst = []

        val = nums[i-1] + nums[i]

        new_lst.append(val % 10)

length = len(new_lst)



"""

from typing import List


class Solution:
    """
    passes leet code
    """
    def triangularSum(self, nums: List[int]) -> int:
        """
        The function to make the traiangular sum 
        """

        #constraintts case 
        if len(nums) == 1 :

            return nums[0]

        #vars 
        length = len(nums)

        while length != 1 :

            new_lst = []

            for i in range(1,length) :

                val = nums[i-1] + nums[i]

                new_lst.append( val%10 )


            #print(new_lst)

            length = len(new_lst)

            nums = new_lst


        return new_lst[0]



sol = Solution()

nums = [1,2,3,4,5]

print(sol.triangularSum(nums))


