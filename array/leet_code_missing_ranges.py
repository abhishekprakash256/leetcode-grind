"""
find the missing ranges 
You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are within the inclusive range.
A number x is considered missing if x is in the range [lower, upper] and x is not in nums.

"""


#test cases
nums = [0,1,3,50,75]
lower = 0
upper = 99
out = [[2,2],[4,49],[51,74],[76,99]]



#test case
nums2 = [-1]
lower2 = -1
upper2 = -1
out2 = []



"""
algo 
two pointer - 

#edge case 
if lem(nums) <= 1
	returnm []





l = 0 
r = l + 1
res_lst = []

#append first logic 
if nums[0] > lower:





strat the toop 
condn r < len(nums)

if nums[r] -  nums[l] == 1 or nums[r] - nums[l] == 0:
	l +=1
	r +=1

elif nums[r] - nums[l] =!1:
	upper = l +1
	lower = r - 1
	res_lst.append([lower,upper])


"""


#incorrect
class Solution():
	def findMissingRanges(self,nums,lower,upper):
		"""
		The function to find the missing ranges in the given values 
		"""

		#cover edge case 
		if len(nums) <=1 :
	
			if nums[0] >= lower or nums[0] >= upper:
				return []

		#initalize the pointers 

		l = 0 
		r = l + 1
		res_lst = []

		while r < len(nums):

			if nums[r] - nums[l] == 1 or nums[r] - nums[l] == 0:
				l +=1
				r +=1

			elif nums[r] - nums[l] !=1:

				upper_val = l +1
				lower_val = r -1
				res_lst.append([lower_val, upper_val])

				r +=1
				l +=1


		return res_lst


sol = Solution()
res = sol.findMissingRanges(nums,lower,upper)

print(res)






















