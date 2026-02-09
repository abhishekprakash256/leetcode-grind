"""
goal is two merge two sorted array using two pointer
"""

nums1 = [1,1,2,3]

nums2 = [1,3,4,5,6]



class Solution():

	def merge_sort(self,nums1 , nums2 ):
		"""
		The function to merge two sorted list
		"""

		#ptrs 
		l , r = 0 ,0 

		#result list
		res = []

		#start the loop
		while l < len(nums1) and r < len(nums2) :

			if nums1[l] <= nums2[r]:

				res.append(nums1[l])

				l += 1

			else :

				res.append(nums2[r])

				r += 1

		#add the remaining elements
		while l < len(nums1) :

			res.append(nums1[l])

			l += 1

		while r < len(nums2) :

			res.append(nums2[r])

			r+= 1
			
		return res



if __name__ == "__main__" :

	sol = Solution()

	res = sol.merge_sort(nums1 , nums2)

	print(res)