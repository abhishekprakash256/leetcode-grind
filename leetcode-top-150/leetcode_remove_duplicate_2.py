"""
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. 
The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. 
More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Custom Judge:


"""

"""
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).



Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).


"""


"""
using a counter of 2 
and two pointer traversal 

Input: nums = [1,1,1,2,2,3]

out = [1,1,2,2,3,_]

brute force approach -- 

using two pointer 
start from 1 position 
move one postion at once 


temp = nusm[0]
ptr = nums[1]

if temp == nums[ptr] and count != 2:
	count +=2 

elif temp == nums[ptr] and count == 2 : 
	count = 0 


else :
	count += 1 
	temp = nums[ptr]

r += 1
temp = nums[r]
total = total + count 

return total


"""

class Solution(object):
	def removeDuplicates_wrong(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		wrong code 
		"""

		#base case 

		if len(nums) == 1:
			return 1


		#make the ptrs 
		seen = False 
		l , r = 0,1
		total = 0 



		#star the loop 
		while r < len(nums):

			if nums[l] == nums[r] and not seen:

				l +=1
				r +=1
				total +=2 
				seen = True

			elif nums[l] == nums[r] and seen:

				l +=1
				r +=1

			else:
				total +=1
				seen = False
				l +=1
				r +=1

		return total


    def removeDuplicates(self, nums: List[int]) -> int:
    	"""
    	passes leet code 

    	"""
        k = 2

        for i in range(2, len(nums)):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1 

        return k





