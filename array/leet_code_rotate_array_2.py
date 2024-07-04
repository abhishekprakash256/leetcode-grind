"""

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]



Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]



1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105


"""

"""
visualization 

1. approach 
brute force 

pop()
insert at zero 


2nd one 
swap use two pointers 

if k == len(nums):
	return nums 

if k < len(nums):
	l = 0 
	r =  len(nums) - k 

	keep swap till k times 

elif k > len(nums):
	res = len(nums) % k 
	l = 0 
	r = len(nums) - k 


Constraints:

    1 <= nums.length <= 105
    -231 <= nums[i] <= 231 - 1
    0 <= k <= 105


Follow up:

    Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
    Could you do it in-place with O(1) extra space?




"""



class Solution:
	def rotate_brurte_force(self, nums, k: int) -> None:
		"""
		Do not return anything, modify nums in-place instead.
		"""

		for i in range(k):

			res = nums.pop()
			nums.insert(0,res)



	#correct code
	def reverse_array(self,l,r):
		"""
		The function to reverse the array 
		"""
		 

		while l < r:

			nums[l] , nums[r] = nums[r] , nums[l]
			r -= 1
			l += 1





	def rotate(self,nums,k):
		"""
		make a optimnal approach 
		"""

		length = len(nums) - 1

		k = k % length  # In case k is larger than the length of nums

		#rotate the whole array 
		l1 = 0 
		r1 = length

		self.reverse_array(l1, r1)


		#rotate the left part 

		l2 = 0 
		r2 = k - 1 

		self.reverse_array(l2,r2)


		#rotate the right part 

		l3 = k
		r3 = length
		

		self.reverse_array(l3,r3)
















nums , k = [1,2,3,4,5,6,7] , 3


if __name__ == "__main__":
	sol = Solution()

	res = sol.rotate(nums,k )

	print(nums)










