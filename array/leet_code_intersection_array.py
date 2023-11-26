"""
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
"""

#test cases 

"""
the question is not solved 

"""

arr1,arr2 = [1,2,3,4], [1,2,3,3]
out1 = [1,2,3]

arr3,arr4 = [3,3,3] , [3,4]
out2 = [3]

arr5, arr6 = [1,2] , [1,2]
out3 = [1,2]

arr7,arr8 = [1,2,3,4] , [5,6,7]
out4 = []

arr9, arr10 = [1,2,2,1] , [2,2]
out5 = [2,2]





class Solution(object):
	def intersect_incorrect(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: List[int]
		"""
		
		left,right  = 0,0  
		intersect_lst = []


		#sort both tha array 
		nums1.sort()
		nums2.sort()


		#make the smaller 
		if len(nums1) <= len(nums2):
			small = nums1
			large = nums2
		else:
			small = nums2
			large = nums1


		while left <= len(small) - 1:

			if small[left] == large[right]:

				intersect_lst.append(small[left])
			
			left +=1
			right+=1

		print(small,large)


		return intersect_lst

	def intersect_incorrect2(self,nums1,nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: List[int]
		"""
		
		left, right = 0,0
		intersect_lst = []


		#make the smaller 
		if len(nums1) <= len(nums2):
			small = nums1
			large = nums2
		else:
			small = nums2
			large = nums1


		while left <= len(small) - 1:

			if small[left] == large[right]:
				intersect_lst.append(small[left])
				left+=1
				right +=1

			elif small[left] < large[right]:
				left +=1

			else:
				right +=1


		return intersect_lst








if __name__ == "__main__":

	sol = Solution()
	res = sol.intersect_incorrect2(arr9,arr10)

	print(res)



			


