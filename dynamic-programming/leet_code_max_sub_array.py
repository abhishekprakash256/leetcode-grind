"""

Given an integer array nums, find the subarray with the largest sum, and return its sum.
"""


"""

nums = [-2,1,-3,4,-1,2,1,-5,4]

out = 6 

sub_arry = [4,-1,2,1]


nums2 = [1,-2,4,6,-10]

nums3 = [-2,1,-3,4]

---------

algo -- 

l = 0 
r = len(nums) - 1
max_sum = 0

while l < r :

	temp_sum = sum(nums[l:r+1])
	max_sum = max(temp_sum,max_sum)

	if nums[l] < nums[r]:
		l +=1

	elif nums[l] > nums[r]:
		r -=1

	else:

		if nums[r+1] > nums[l-1]:
			r -=1

		else:
			l +=1 


return max_sum


"""




nums = [-2,1,-3,4,-1,2,1,-5,4]



#wrong code ----
class Solution:
	def maxSubArray(self, nums) -> int:
		"""
		The function to find the max sub array
		"""
		
		#base case 
		if len(nums) == 1:
			return nums[0]
		
		#initilaize the vars
		l = 0 
		r = len(nums) - 1 
		max_sum = 0 
		
		while l < r:
			
			#calc
			temp_sum = sum(nums[l:r+1])
			max_sum = max(temp_sum,max_sum)
			
			#condn
			if nums[l] < nums[r]:
				l +=1
			
			elif nums[l] > nums[r]:
				r -=1
			
			else:
				
				if nums[l+1] > nums[r-1]:
					r -=1
				else:
					l +=1
		
		return max_sum



if __name__ == "__main__":

	sol = Solution()

	res = sol.maxSubArray(nums)


	print(res)