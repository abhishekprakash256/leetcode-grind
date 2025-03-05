"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""


"""

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Example 3:

Input: nums = [1,0,1,2]
Output: 3

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109


"""


"""
approach -- 

make the list as a set remove the duplicate issue

after that make check for the length 

check if the left neighbor exists in the list 

iterate over the 


"""




class Solution():
    """
    passes leetcode
    """
    def longestConsecutive(self,nums):
        """
        The function to find the longest sequence in the array in O(n) time
        """

        #constarint case 
        if not nums:

            return 0 

        if len(nums) == 1 :

            return 1


        #make the list as set 
        nums = set(nums)

        #vars 
        longest = 0 

        for num in nums :

            #check if left neighbor
            if num - 1 not in nums:

                length = 0 

                #search the array 
                while (num + length) in nums:

                    length += 1 

                longest = max(length, longest)

        return longest













