"""
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. I
f the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.
"""

"""

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

 

Constraints:

1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.



"""


"""

approach -- 


use a binary search and move as per small side 

if both are equal move one side 

in the last return one side that is higher 


"""


class Solution_slow():

	def findPeakElement(self,nums):
		"""
		The function to find the peak elemmen in logn time
		passes leetcode
		o(n) time 
		"""

		#constraints case 
		if len(nums) == 1:
			return 0


		#make the ptr
		l , r = 0 , len(nums) - 1 


		while l <= r :

			if nums[l] <= nums[r] :

				l += 1 

			else:

				r -= 1 

		return l - 1




class Solution:

    def findPeakElement(self, nums):
        """
        Function to find a peak element in O(log n) time.
        A peak element is an element that is greater than or equal to its neighbors.
        """
        # Handle edge case: single element array
        if len(nums) == 1:
            return 0

        # Binary search for peak element
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # Compare middle element with its right neighbor
            if nums[mid] > nums[mid + 1]:
                # Move to the left half
                right = mid
            else:
                # Move to the right half
                left = mid + 1

        # At the end, left and right converge to the peak element
        return left
