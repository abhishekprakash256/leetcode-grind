"""
give an array of the integers , find the higest product we can get by multiplying 3 elements
"""

"""
constartint -- 

3<= n <=5e5

[1,2,0,3]

1*2*3 == 6

[-1,-2, 0,0,2]

(-1) * (-2) * 2 = 4

[-2,3,4,5,0,1]

sorting 

[0,1,2,3]

max = last 3 elemnts 


[-1,-2, 0,0,2]


max = min(first two ) * last 


sort 

first two * last 

[-6, -5 , -4, -3 , -2]


last 3 

if 0 then case changes 

[-1,0,5,6,7]

sorted(nums)

h1 = nums[0] * nums[1] * nums[len(nums) - 1]

h2 = nums[-1] * nums[-2] * nums[0-3]

"""

class Solution:
	def maximumProduct(self, nums: List[int]) -> int:

		nums.sort()

		h1 = nums[0] * nums[1] * nums[-1]

		h2 = nums[-1] * nums[-2] * nums[-3]

		return max(h1,h2) 
		