"""

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
"""


#test cases 

nums = [4,5,6,7,0,1,2]
target = 0
out = 4 


nums2 = [4,5,6,7,0,1,2]
target2 = 5
out2 = 1 

nums3 = [8,9,1,2,3,4,5,6]

nums4 = [1,2,3,4,5,0]

"""
sudo soln 

binary search 

base case 
	if len(nums) == 1:
		if nums[0] == target:
			return 0 

		else: 
			return -1


#initilaization of vars 
l = 0
r = len(nums) - 1

while l <= r :

	mid = (l + r) // 2
	
	#binary search 
	if nums[mid] == target:
		return mid

	elif nums[l] < muns[mid] < nums[r]:

		if target < nums[mid]:
			r = mid - 1

		else:
			l = mid + 1

	
	elif nums[l] > nums[mid]:

		if target > nums[mid]:


			



	


		


"""

