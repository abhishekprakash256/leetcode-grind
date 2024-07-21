"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

	Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
	Return k.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
	assert nums[i] == expectedNums[i];
}

If all assertions pass, then your solution will be accepted.


Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

"""



"""
--------------------Thinking -----------------


sorted in increasing order 
remove in place 
the relative order is same 
return the unique number of the elements 



1. brute force 

- use a hashmap 
- see the element store it 
- see it again remove it and proceed 
- if not in hashmap count it and return it 
	- return the len(hashmap)
- order will remain same as well 



2. using two pointer 









"""

#test case 

#edge case 
nums0 = [1,1,2]
out0 = 0

nums1 = [1,1,1,1,3]
out1 = 2


nums2 = [1,1,1,3,3,4,4,4]
out2 = 3







class Solution:
	def removeDuplicates_slow(self, nums) -> int:
		"""
		The function to remove the repeated elemnts and return the number of unique elements
		#working code passed all tests in leetcode
		"""

		#edge case 
		if len(nums) == 0:
			return 0 

		if len(nums) ==1 :
			return 1


		#hashmap 
		mapper = {}

		#count the num unique elemenst 
		count = 0

		#iterator
		i = 0 

		#length of array 
		length = len(nums)


		#start the loop 
		while i < length:

			if nums[i] not in mapper:

				mapper[nums[i]] = True
				count += 1
				i += 1

			else:

				nums.pop(i)

			length = len(nums)


		return count


	def removeDuplicates(self, nums) -> int:
		"""
		The function to remove the repeated elements and return the number of unique elements.
		works the code and passsed in leet code 
		"""

		# Edge case: if the list is empty, return 0
		if len(nums) == 0:
			return 0

		l, r = 0, 1

		while r < len(nums):
			if nums[l] == nums[r]:
				nums.pop(r)
			else:
				l += 1
				r += 1

		return len(nums)


if __name__ == "__main__":
	sol = Solution()

	res = print(sol.removeDuplicates(nums0))
	print(res)












		