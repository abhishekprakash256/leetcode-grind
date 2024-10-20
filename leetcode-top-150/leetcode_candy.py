"""
here are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

	Each child must have at least one candy.
	Children with a higher rating get more candies than their neighbors.

Return the minimum number of candies you need to have to distribute the candies to the children.

"""

"""
Example 1:

Input: ratings = [1,0,2]
[2,1,2]

Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.


[1,2,2]
[1,2,1]


[0,0,1]

1,1,2





"""




class Solution:
	def candy(self, ratings) -> int:
		"""
		The function to find the number of the candy needed 
		"""

		#make the array with rating with 1 
		arr = [1] * len(ratings)

		
		#make the array have more than value of the neighbour array 
		for i in range(1,len(ratings)):

			if ratings[i-1] < ratings[i]:
				arr[i] = arr[i-1] + 1


		#make the array to have more values 
		for i in range(len(ratings) - 2, -1, -1):

			if ratings[i] > ratings[i+1]:
				arr[i] = max(arr[i], arr[i + 1] + 1)

		return sum(arr)



sol = Solution()

print(sol.candy([1,0,2]))











