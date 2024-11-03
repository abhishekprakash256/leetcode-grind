"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

"""

"""
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


"""



"""

#base case 

if len(nums) == 1:
	return [nums[0]]


use one loop 

res_lst = []


for i in range(1,len(intervals)):

	if intervals[i][0] <= intervals[i-1][1] :

		res_lst.append([intervals[i-1][0], intervals[i][1]])


	else:



"""

from typing import List


class Solution:
	def merge(self, intervals: List[List[int]]) -> List[List[int]]:
		"""
		The function to merge the intervals
		passes leetcode
		"""

		#base case 
		if len(intervals) == 1:

			return [intervals[0]]


		#sort the list 
		intervals.sort( key = lambda i : i[0] )

		print(intervals)

		#make vars
		i = 1

		while i < len(intervals):

			#the condn

			if intervals[i-1][1] >= intervals[i][0] :


				#first and last val check 
				if intervals[i-1][1] >= intervals[i][1] :

					first = intervals[i-1][0]
					second = intervals[i-1][1]

					intervals.pop(i-1)
					intervals.pop(i-1)

					intervals.insert(i-1,[first,second])


				else:

					#add the element 
					first = intervals[i-1][0]
					second = intervals[i][1]


					intervals.pop(i-1)
					intervals.pop(i -1)

					#add the elemenmt in the intervals
					intervals.insert(i-1,[first,second])


			else:

				i += 1


		return intervals





sol = Solution()

print(sol.merge([[10,16],[2,8],[1,6],[7,12]]))


















