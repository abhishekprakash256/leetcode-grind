"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.

"""

nums = [-2,1,-3,4,-1,2,1,-5,4]
out = 6 , #[4,-1,2,1]


nums2 = [1]
out2 = 1

nums3 = [5,4,-1,7,8]
out3 = 23


"""
algo -- 

brute force 

n^2 with each iteration 
giving the max val 


-----

optim Algo -- 

#base case
if len(nums) == 1:
	return nums[0]

l = 0

max_sum = 0 

#start the loop 

for r in range(1,len(nums)):

	temp_sum = sum(nums[l:r+1])

	if temp_sum < 0 :
		l = r 

	max_sum = max(temp_sum,max_sum)


return max_sum



"""

#-----------------------------incorrect -------------------------
class Solution():

	def maxSubArray_incorrect(self,nums):
		"""
		The function to find the max sub array of the given array 
		"""

		#base case 
		if len(nums) == 1 :
			return 0 


		#vars 
		l = 0 
		max_sum = 0 

		#start the window 
		for r in range(1,len(nums)):

			temp_sum = sum(nums[l:r+1])
			print(l)

			if temp_sum < 0 :
				l = r

			max_sum = max(temp_sum,max_sum)


		return max_sum


	def maxSubArray(self,nums):
		"""
		The fucntion to find the max sub aray of the nums 
		"""

		#base case 
		if len(nums) == 1:
			return nums[0]


		cur_sum = 0
		max_sum = nums[0]

		for n in nums:

			#calc the temp sum 
			if cur_sum < 0 :
				
				cur_sum = 0 

			cur_sum +=n

			max_sum = max(max_sum,cur_sum)

		return max_sum









if __name__ == '__main__':

	sol = Solution()

	print(sol.maxSubArray(nums))

























