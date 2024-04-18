"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

"""


"""
explanation -- 

nums = [5,7,7,8,8,10] 
target = 8

out = [3,4]


if not found give [-1.-1]


#comstraints 


0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109



#base case 

res = [-1.-1] 

if len(nums) == 0: 
	return res



#simple binary search 

l,r = 0 , len(nums) - 1 

#start the loop 

while l <= r : 

	mid = (l+ r )//2 

	if nums[m] == target:
		found = True 
		break

	elif nums[m] < target :
		r = m - 1

	else:
		l = m + 1


if found:

	for i in range(m,len(nums)-1):

		if nums[m] != nums[i]:
			res[1] = i-1


	for j in reversed(range(m,0)):

		if nums[m] != nums[j]:
			res[0] = i +1 

	return res

else:
	return res


"""

nums = [5,7,7,8,8,10] 
target = 8


class Solution():

	def searchRange(self,nums,target):
		"""
		The function to find the target range in the nums array 
		"""

		#make the res lst
		res = [-1,-1]


		#base case
		if len(nums) == 0 :
			return res

		l , r = 0 , len(nums) - 1 
		found = False


		#start the loop 

		while l <= r : 

			m = (l + r ) // 2 

			if nums[m] == target:
				found = True
				break

			elif nums[m] < target:
				l = m + 1 

			else:
				r = m - 1


		if not found:
			return res

		else:

			for i in range(m,len(nums) - 1 ):

				if nums[m] != nums[i]:
					res[1] = i - 1

			for j in rrange(m,0,-1):

				if nums[m] != nums[i]:
					res[0] = i + 1

			return res

 

if __name__ == "__main__":

	sol = Solution()

	print(sol.searchRange(nums,target))




