"""
A sequence x1, x2, ..., xn is Fibonacci-like if:

    n >= 3
    xi + xi+1 == xi+2 for all i + 2 <= n

Given a strictly increasing array arr of positive integers forming a sequence, return the length of the longest Fibonacci-like 
subsequence of arr. 
If one does not exist, return 0.

A subsequence is derived from another sequence arr by deleting any number of elements (including none) from arr, 
without changing the order of the remaining elements. For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].
"""

"""
Example 1:
              - - - - - - - -
Input: arr = [1,2,3,4,5,6,7,8]
Output: 5
Explanation: The longest subsequence that is fibonacci-like: [1,2,3,5,8].

Example 2:
              - - -  -  -  -  - 
Input: arr = [1,3,7,11,12,14,18]
Output: 3
Explanation: The longest subsequence that is fibonacci-like: [1,11,12], [3,11,14] or [7,11,18].

 

Constraints:

3 <= arr.length <= 1000
1 <= arr[i] < arr[i + 1] <= 109


"""


"""
approach -- 

constaintr case 

if len(arr) == 3:
	check and return

brute force 

can work but with O(n^2)

check all the possibllities

make a set for the arry 

make a hashmap for store the values for the addition if arry has 



"""

from typing import List

class Solution():
    """
    passess leetcode
    """
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        """
        Function to find the max length of the Fibonacci-like subsequence.
        """

        # Edge case: If length is less than 3, return 0
        if len(arr) < 3:
            return 0 

        # Convert arr to set for quick lookup
        set_arr = set(arr)

        mapper = {}
        max_len = 0

        for i in range(len(arr)):
            
            for j in range(i):
                
                # Check if arr[i] and arr[j] can form a Fibonacci-like sequence
                if arr[i] - arr[j] in set_arr and arr[i] - arr[j] < arr[j]: 
                    
                    prev = arr[i] - arr[j]
                    # Extend the sequence if it exists in mapper, otherwise start a new one
                    mapper[(arr[j], arr[i])] = mapper.get((prev, arr[j]), 2) + 1
                    max_len = max(max_len, mapper[(arr[j], arr[i])])


        return max_len if max_len >= 3 else 0





