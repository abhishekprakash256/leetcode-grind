"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?
"""

nums = [3,2,1,5,6,4]
k = 2

out = 5 

"""
Algo - 

[1,2,3,4,5,6]

max_val = nums[0]
k = 2 
count = 0 

[3,2,1,5,6,4]

The solution can be done using a heap datastracuture 





"""



import heapq

class Solution:
    def findKthLargest(self,nums, k):
        min_heap = []
        
        # Initialize the min-heap with the first k elements of nums
        for i in range(k):
            heapq.heappush(min_heap, nums[i])

        #print(min_heap)
        
        # Iterate through the remaining elements of nums
        for i in range(k, len(nums)):
            # If the current element is greater than the root of the min-heap,
            # replace the root with the current element
            if nums[i] > min_heap[0]:
                #print(min_heap)
                heapq.heappop(min_heap)
                #print(min_heap)
                heapq.heappush(min_heap, nums[i])
                #print(min_heap)
        
        # The root of the min-heap will be the kth largest element
        return min_heap[0]

        
