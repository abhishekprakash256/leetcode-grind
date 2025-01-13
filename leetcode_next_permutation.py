"""
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].

The next permutation of an array of integers is the next lexicographically greater permutation of its integer. 

More formally, if all the permutations of the array are sorted in one container according to their lexicographical order,
then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, 
the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.

Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

"""

"""
Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]

 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100


"""


class Solution():

	def next_permutation(nums):
		"""
		Rearranges the list `nums` into the lexicographically next permutation.
		If such arrangement is not possible, it rearranges into the lowest possible order.
		passese leetcode
		"""
		# Step 1: Find the pivot
		pivot = -1

		for i in range(len(nums) - 2, -1, -1):  # Start from the second last element
			if nums[i] < nums[i + 1]:
				pivot = i
				break

		if pivot == -1:
			# If no pivot found, reverse the array to get the smallest permutation
			nums.reverse()
			return

		# Step 2: Find the smallest element larger than nums[pivot] to the right
		for i in range(len(nums) - 1, pivot, -1):
			if nums[i] > nums[pivot]:
				# Step 3: Swap the pivot and this element
				nums[i], nums[pivot] = nums[pivot], nums[i]
				break

		# Step 4: Reverse the suffix (everything to the right of pivot)
		nums[pivot + 1:] = reversed(nums[pivot + 1:])