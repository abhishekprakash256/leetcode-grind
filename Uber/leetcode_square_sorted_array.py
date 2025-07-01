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



- compare the abs value -- 
- move the pointer to left to right 
- greater value swap and move the right poniter 

if abs(left) greater than abs(right) , swap move the right poniter  

else move right , euqal move the right 



3,-3,2,7,11

2,-3,3,7,11








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



	def sortedSquares(self,nums):
		"""
		The function to get the sorted array of the squares of the original
		"""

		#ptrs
		l , r = 0 ,len(nums) - 1

		#sawp tthe array
		while l <= r :

			if abs(nums[l]) > abs(nums[r]) :

				nums[l] , nums[r] = nums[r] , nums[l]

				l += 1

			else :

				r -= 1

		#square the elments 
		for i in range(0,len(nums)) :

			nums[i] = nums[i]*nums[i]

		return nums











if __name__ == "__main__":

	sol = Solution()

	nums = [-7,-3,2,3,11]

	res = sol.sortedSquares(nums)


	#print
	print(res)



