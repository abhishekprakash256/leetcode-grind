"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. 
The remaining elements of nums are not important as well as the size of nums.
Return k.



"""


"""

algo 

1. using hash map 

one iteration see the elemnt 
put in hash map 
the compare if present remove the elemnt and append the _ in last  

if not present add and skip it 


2. using two pointer 

#edge case of one leenmnt or zero in array 

start the two pointer 
compare the values 
if same remove and put the next pointer to next element , append in the last as well 
else move both to next pointer



"""




class Solution(object):
	def removeDuplicates(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""

		#edge case 
		if len(nums) == 0 or len(nums) == 1:
			return nums 

		#initilize the mapper 
		mapper = {}
		count = 0 


		#start the loop 
		for i in range(len(nums)):	

			if nums[i] not in mapper:
				mapper[nums[i]] = True

			else:
				count +=1
				nums.pop(i)
				nums.append("_")

		return len(mapper)
			

		






if __name__ == "__main__":

	sol = Solution()

	nums = [0,0,1,1,1,2,2,3,3,4]

	print(sol.removeDuplicates(nums))

	print(nums)


