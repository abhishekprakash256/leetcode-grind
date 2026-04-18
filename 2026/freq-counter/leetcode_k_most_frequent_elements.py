"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 
"""

"""

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]

Example 2:

Input: nums = [1], k = 1

Output: [1]

Example 3:

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

Output: [1,2]


"""

"""

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size

"""

"""
approach - 

I can make the counter 

then sort the items on vals O (nlogn)

how to make faster ? 

brute force solution 

sorted_map = sorted(frequency_map.items(), key=lambda x:x[1], reverse=True)

final_lst = []

for i in sorted_map:
	final_lst.append(i[0])
return final_lst[0:k]


how do I optimize  ?

using the bucket sort it can be optimized 

put the elemnts in the bucket and sort out 


"""

from typing import List
from collections import Counter





class Solution:
	def topKFrequent(self, nums: List[int], k: int) -> List[int]:
		"""
		The function to find the top k sorted elements
		"""

		#make the freq dict
		freq_mapper = Counter(nums)

		#make the bucket
		bucket = []

		#result list
		res = []

		for i in range(len(nums)+1):

			bucket.append([])

		#print(freq_mapper)
		#print(bucket)

		#append the freq into the bucket
		for i in freq_mapper.items():

			bucket[i[1]] = [i[0]]


		#print(bucket)

		#return the k elemnts
		# traverse from high freq → low
		for i in range(len(bucket) - 1, 0, -1):
			for num in bucket[i]:
				res.append(num)
				if len(res) == k:
					return res






class Solution_w:
	def topKFrequent(self, nums: List[int], k: int) -> List[int]:
		
		freq = Counter(nums)

		# bucket index = frequency
		bucket = [[] for _ in range(len(nums) + 1)]

		print(bucket)

		# fill buckets
		for num, f in freq.items():
			bucket[f].append(num)

		print(bucket)

		res = []

		# traverse from high freq → low
		for i in range(len(bucket) - 1, 0, -1):
			for num in bucket[i]:
				res.append(num)
				if len(res) == k:
					return res






if __name__ == "__main__":

	nums = [1,1,1,2,2,3]

	nums = [1,2,1,2,1,2,3,1,3,2]

	k = 2

	sol = Solution()

	res = sol.topKFrequent(nums , k )

	print(res)

