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

class Solution:
	def merge(self, intervals: List[List[int]]) -> List[List[int]]:
		"""
		The function to merge the intervals
		"""

		#base case 
		if len(intervals) == 1:

			return [intervals[0]]


		#result list 
		res_lst = []


		#start the loop
		for i in range(1,len(intervals)):

			#condn

			if intervals[i][0] <= intervals[i-1][1] :

				first = intervals[i-1][0]


			else:

				res_lst.append([first,intervals[i][1]])


		return res_lst















