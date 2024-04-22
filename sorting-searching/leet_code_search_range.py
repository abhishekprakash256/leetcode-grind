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

nums = [2,2] 
target = 2



# soln 

class Solution:
    def searchRange(self, nums, target):
        """
        Find the target range in the nums array 
        """
        res = [-1, -1]

        # Base case
        if not nums:
            return res

        # Binary search to find the leftmost index of the target
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if nums[left] != target:
            return res
        res[0] = left

        # Binary search to find the rightmost index of the target
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2 + 1  # Adjusted mid calculation
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid
        res[1] = right

        return res



if __name__ == "__main__":

	sol = Solution()

	print(sol.searchRange(nums,target))




