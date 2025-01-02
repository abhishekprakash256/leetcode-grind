"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

"""


"""
Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

 

Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104


"""




"""





"""

import heapq

# Create a min-heap
heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 4)
heapq.heappush(heap, 2)

print("Heap:", heap)  # [1, 2, 4, 3]

# Extract the minimum element
min_element = heapq.heappop(heap)

print("Extracted Min:", min_element)  # 1
print("Heap after extraction:", heap)  # [2, 3, 4]




class Solution():
	"""
	Passes leetcode
	"""

	def findKthLargest(self, nums: List[int], k: int) -> int:
		"""
		The function to find the kth largest element
		"""

		#constarints 
		if len(nums) == 1:

			return nums[0]


		#make the heap
		min_heap = []

		for num in nums:

			heapq.heappush(min_heap,num)


			if len(min_heap) > k :

				heapq.heappop(min_heap)

		return min_heap[0]




