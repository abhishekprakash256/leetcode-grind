"""
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least 
h papers that have each been cited at least h times.

"""

"""
Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.



Input: citations = [1,3,1]
Output: 1


"""



"""

first find max 

max = (len(nums) % 2) + 1 

[0,1,3,5,6]

[1,1,3]

brute force approach -- 

[1,1,3] odd length len(nums) % 2 

[1,2,4,5]

(len(nums)%2) - 1 

a = [5, 2, 9, 1, 5, 6]

# Sort the value in increasing order
a.sort()
print(a)

"""



class Solution():

	def hIndex(self, citations) -> int:
		"""
		Find the h index in the array
		"""

		#base case 
		if len(citations) == 1:
			if citations[0] == 0 :
				return 0
			else:
				return 1

		#set the flag
		even = False 


		#check the true and false
		if len(citations)%2 == 0:
			even = True

		#sort the element
		citations.sort()

		#check the mid element 
		if even:

			ele = (len(citations) // 2 ) - 1

		else:
			ele = (len(citations) // 2 )


		return citations[ele]






if __name__ == '__main__':
	sol = Solution()
	print(sol.hIndex([3,0,6,1,5]))





