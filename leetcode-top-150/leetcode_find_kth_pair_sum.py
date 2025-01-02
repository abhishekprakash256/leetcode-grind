"""
You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an 
integer k.

Define a pair (u, v) which consists of one element from the first array and one element 
from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

"""

"""
Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]


Constraints:

1 <= nums1.length, nums2.length <= 105
-109 <= nums1[i], nums2[i] <= 109
nums1 and nums2 both are sorted in non-decreasing order.
1 <= k <= 104
k <= nums1.length * nums2.length


"""

"""
approach -- 

usng a min heap 

append the first value till the length of the array 

starting the first ptr 

push the elemnst in the min heap

then pop the elemnt and add the more value as per k value 

"""

class Solution():

	def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[Tuple[int, int]]:
		"""
		The functotion to find the smallest sum pairts in the array 
		"""

		#constarints 
		if not nums1 or not nums2 or k <= 1 :

			return []


		#make the heap 
		min_heap = []

		#make the res list 
		res_lst = [] 


		#append the first elements 
		for j in range(min(k,len(nums2))) :

			heapq.heappush(min_heap,(nums1[0] + nums2[j] ,0,j))


		while k > 0 and min_heap :

			#pop the element 
			curr_sum , i, j = heapq.heappop(min_heap)

			#append in the res list 
			res_lst.append([nums1[i],nums2[j]])

			if i + 1 < len(nums2) :

				#put the recent element
				heapq.heappush(min_heap,(nums1[i+1] + nums2[j],i+1,j))

			k -=1


		return res_lst



