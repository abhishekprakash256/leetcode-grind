"""
Your country has 109 lakes. Initially, all the lakes are empty, but when it rains over the nth lake, the nth lake becomes full of water. 
If it rains over a lake that is full of water, there will be a flood. Your goal is to avoid floods in any lake.

Given an integer array rains where:

	rains[i] > 0 means there will be rains over the rains[i] lake.
	rains[i] == 0 means there are no rains this day and you must choose one lake this day and dry it.

Return an array ans where:

	ans.length == rains.length
	ans[i] == -1 if rains[i] > 0.
	ans[i] is the lake you choose to dry in the ith day if rains[i] == 0.

If there are multiple valid answers return any of them. If it is impossible to avoid flood return an empty array.

Notice that if you chose to dry a full lake, it becomes empty, but if you chose to dry an empty lake, nothing changes.
"""


"""
Example 1:

Input: rains = [1,2,3,4]
Output: [-1,-1,-1,-1]
Explanation: After the first day full lakes are [1]
After the second day full lakes are [1,2]
After the third day full lakes are [1,2,3]
After the fourth day full lakes are [1,2,3,4]
There's no day to dry any lake and there is no flood in any lake.

Example 2:

Input: rains = [1,2,0,0,2,1]
Output: [-1,-1,2,1,-1,-1]
Explanation: After the first day full lakes are [1]
After the second day full lakes are [1,2]
After the third day, we dry lake 2. Full lakes are [1]
After the fourth day, we dry lake 1. There is no full lakes.
After the fifth day, full lakes are [2].
After the sixth day, full lakes are [1,2].
It is easy that this scenario is flood-free. [-1,-1,1,2,-1,-1] is another acceptable scenario.

Example 3:

Input: rains = [1,2,0,1,2]
Output: []
Explanation: After the second day, full lakes are  [1,2]. We have to dry one lake in the third day.
After that, it will rain over lakes [1,2]. It's easy to prove that no matter which lake you choose to dry in the 3rd day, the other one will flood.

 

Constraints:

	1 <= rains.length <= 105
	0 <= rains[i] <= 109


"""


"""
approach -- 

using a lazy greedy 

if see a dry day store the value and dry that later the lake if occurs again 

unless the lake is not repeating no drying is happening. 

list_lake = []

res = [-1]*len(rains)

#if first found a dry day
if rains[i] == 0 :

	list_lake.append(i)

if days are repeating then find the next dry day

using the binay search algo 









"""

from typing import List
import bisect


class Solution_w:
	def avoidFlood(self, rains: List[int]) -> List[int]:
		"""
		The function to find the avoid flood for the city
		"""

		#storage
		dry_days = []
		rain_days = {}
		res = [-1] * len(rains)

		#loop the rain days
		for i in range(len(rains)) :

			#if a dry day
			if rains[i] == 0 :

				dry_days.append(i)


			#if the same rain day found
			while rains[i] in rain_days :

				#if we have dry days
				if len(dry_days) > 0:

					dry_day_num = dry_days.pop(0)

					res[dry_day_num] = rains[i] 

				#if we don't have dry day yet
				else :
					
					dry_day_num = bisect.bisect_right(rains, 0 )

					res[dry_day_num] = rains[i]

				#remove from the dict
				del rain_days[rains[i]]


			#add in the rain days dict
			rain_days[rains[i]] = True


		return res



class Solution():
	
	def avoidFlood(self, rains: List[int]) -> List[int]:
		"""
		The function to avoid flood for the city
		"""

		#vars 
		dry_days = []
		rain_days = {}
		res = [-1] * len(rains)

		#loop over the rain days 
		for i in range(len(rains)) :

			#if a dry day 
			if rains[i] == 0 :

				res[i] = 1  # placeholder
				dry_days.append(i)

				continue 

			lake = rains[i]

			#if not a dry day
			if lake in rain_days :

				last_rain_day = rain_days[lake] 

				#find the next rain day to dry 
				idx = bisect.bisect_right(dry_days, last_rain_day)

				#if no dry day available 
				if idx == len(dry_days) :

					return []

				dry_day_index = dry_days[idx]

				#assign the data in res
				res[dry_day_index] = lake

				#remove from the pool 
				dry_days.pop(idx)


			#mark as full day
			rain_days[lake] = i 

			res[i] = -1

		return res

























if __name__ == "__main__":

	sol = Solution()

	rains = [1,2,3,4]

	rains = [1,2,0,0,2,1]

	res = sol.avoidFlood(rains)

	print(res)