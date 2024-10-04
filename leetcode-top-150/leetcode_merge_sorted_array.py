"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. 
nums2 has a length of n.

"""

"""
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.


Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].


Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

"""


"""



"""


class Solution():

	def merge_brute_one(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
		"""
		The function to make merge the sorted array
		deosn't modify in place and gives wrong output

		"""

		#megre the sorted array
		nums1 = nums1[:m+1] + nums2

		nums1.sort()


		return None


	def merge_brute_two(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
		"""
		The function to mege in the place 
		return none
		passes leetcode beats 74% solution

		"""
		j = 0

		for i in range(m,len(nums1)):

			nums1[i] = nums2[j]
			j +=1


		nums1.sort()

		return None

	def merge(self, nums1, m, nums2, n):
		"""
		Merge sorted array nums2 into nums1 in-place.
		:param nums1: List[int] - First sorted array with extra space at the end
		:param m: int - Number of valid elements in nums1
		:param nums2: List[int] - Second sorted array
		:param n: int - Number of valid elements in nums2
		:return: None - Modifies nums1 in-place
		passes the leet code soluion
		"""

		last = m + n - 1  # Last index of the merged array

		# Merge in reverse order
		while m > 0 and n > 0:
			if nums1[m - 1] > nums2[n - 1]:
				nums1[last] = nums1[m - 1]  # Use the element from nums1
				m -= 1
			else:
				nums1[last] = nums2[n - 1]  # Use the element from nums2
				n -= 1
			last -= 1

		# If there are remaining elements in nums2, place them in nums1
		while n > 0:
			nums1[last] = nums2[n - 1]
			n -= 1
			last -= 1

		# No need to return anything as we are modifying nums1 in-place
















