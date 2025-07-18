"""

Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.
"""


"""

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].



Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]


"""


"""


Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.

 
Follow up: Squaring each element and sorting the new array is very trivial, 
could you find an O(n) solution using a different approach?


"""


"""

[-7,-3,2,3,11]

49,9,4,6,121 

[4,9,9,49,121]

compare the values --> 

left and right compare the abs value

where ever is less we move that pointer 


untill mid clashse 




[-4,-1,0,3,10]




"""



from typing import List



class Solution:
	def sortedSquares_brute(self, nums: List[int]) -> List[int]:
		"""
		The function to get the sorted array of the sqaures of the orginial 
		"""	

		#the resulted array of the integers 
		res = []

		#loop to make the square
		for num in nums: 

			res.append(num*num)

		#sort the array
		res.sort()

		#return the res
		return res



    def sortedSquares(self, nums):
        """
        Returns a sorted array of the squares of the elements from the input array.
        """
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        pos = n - 1  # Fill from the end

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[pos] = nums[left] ** 2
                left += 1
            else:
                result[pos] = nums[right] ** 2
                right -= 1
            pos -= 1

        return result










if __name__ == "__main__":

	sol = Solution()

	nums = [-7,-3,2,3,11]

	res = sol.sortedSquares(nums)


	#print
	print(res)



