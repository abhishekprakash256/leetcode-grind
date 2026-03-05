"""
You are given an integer length and an array updates where updates[i] = [startIdxi, endIdxi, inci].

You have an array arr of length length with all zeros,
 and you have some operation to apply on arr. In the ith operation, 
 you should increment all the elements arr[startIdxi], arr[startIdxi + 1], ..., arr[endIdxi] by inci.

Return arr after applying all the updates.
"""

"""
Input: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
Output: [-2,0,3,5,3]

Example 2:

Input: length = 10, updates = [[2,4,6],[5,6,8],[1,9,-4]]
Output: [0,-4,2,2,2,4,4,-4,-4,-4]


Constraints:

1 <= length <= 105
0 <= updates.length <= 104
0 <= startIdxi <= endIdxi < length
-1000 <= inci <= 1000



"""

"""

approach -- 

make the array of 0s 

add the num to the limit by iterration 

then sum the array


"""
from typing import List

class Solution:
	def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
		"""
		The function to make the array range
		"""

		#make the diff array
		diff = [0] * length

		#make the limits ptrs
		for l ,r , val in updates:

			diff[l] += val

			if r + 1 < length :

				diff[r+1] -= val

		#make the res array
		res = [0] * length
		res[0] = diff[0]

		#make the res array
		for i in range(1,length):

			res[i] = res[i - 1] + diff[i]

		return res



if __name__ == '__main__':
	sol = Solution()

	length = 5
	updates = [[1,3,2],[2,4,3],[0,2,-2]]

	res = sol.getModifiedArray(length , updates)

	print(res)