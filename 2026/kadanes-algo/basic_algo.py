"""
the basic kadane algo file
"""
def maxSubArray(nums):
	curr_sum=nums[0]
	max_sum=nums[0]
	
	for i in range(1,len(nums)):
		curr_sum=max(nums[i],curr_sum+nums[i])
		max_sum=max(max_sum,curr_sum)
		
	return max_sum




if __name__ == "__main__" :

	nums = [1,-2,3,-1,3,5,-3]

	res = maxSubArray(nums)

	print(res)