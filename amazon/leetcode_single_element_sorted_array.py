"""
You are given a sorted array consisting of only integers where every element appears exactly twice, 
except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.
"""

"""

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 105

"""


"""
approach -- 

constraint case 

return first elemet 

sorted 

O(logn)

using binary search but how ? 


[1,1,2,3,3,4,4,8,8]

[1,1,2,2,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11]

how to move the left and the right pointer ? 

how to decide  move towrds the value 2 ? 

exacyly appears twice ? 

and one appeacr once ? 

the length of array is odd 

[1,1,2,3,3,4,4,8,8]

if mid % 2 == 1 :
    mid -= 1 

if nums[mid] == nums[m-1] :

    r = mid -1 

else :
    l = mid + 1

return nums[low]
"""


class Solution():
    """
    passes leetcode
    """

    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        The functon to find the one value in the array
        """

        #constraint case 
        if len(nums) == 1 :

            return nums[0]

        #ptrs
        l , r = 0 , len(nums) - 1 

        while l < r :

            m = (l + r ) //  2

            if m % 2 == 1 :

                m -= 1 

            if nums[m] == nums[m+1] :

                l = m + 2  

            else :

                r = m

        return nums[l]