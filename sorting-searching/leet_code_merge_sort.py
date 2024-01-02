"""
given the two arrays sort as the merge sort 
"""

#test cases 
numsone1 = [1,3,4,0,0,0]
numsone2 = [2,2,2]
out1 = [1,2,2,2,3,4]


numstwo1 = []
numstwo2 =[1]
out2 = [1]


numsthree1 = [1,5,10]
numsthree2 = []
out3 = [1,5,10]


#corect soln 
class Solution:
	def merge(self, nums1, m, nums2, n: int):
		"""
		Do not return anything, modify nums1 in-place instead.
		"""

		#remove the zeros from either list 
		while len(nums1)!=0:

			#remove the zeros 
			ele = nums1.pop(-1)
			if ele == 0 :
				continue
			else:
				nums1.append(ele)
				break
		
		while len(nums2) !=0:
			#remove the zeros 
			ele2 = nums2.pop(-1)
			if ele2 == 0 :
				continue
			else:
				nums2.append(ele2)
				break


		#make the storing array 
		new_lst = []

		#initilaize the two pointers 
		l,r = 0,0 

		#start the loop 

		while l < len(nums1) and r < len(nums2): 

			#make the comparision 
			if nums1[l] < nums2[r] : 

				new_lst.append(nums1[l])
				l +=1

			elif nums1[l] > nums2[r]: 

				new_lst.append(nums2[r])
				r +=1

			else:
				new_lst.append(nums1[l])
				new_lst.append(nums2[r])
				l +=1
				r +=1
			
		# for the remaining elements 
		while l < len(nums1):

			new_lst.append(nums1[l])
			l +=1

		while r < len(nums2): 

			new_lst.append(nums2[r])
			r+=1
		
		return new_lst



if __name__ == "__main__":

	sol = Solution()
	res = sol.merge(numsone1,3, numsone2,3)

	res2 = sol.merge(numstwo1,3, numstwo2,3)

	res3 = sol.merge(numsthree1,3, numsthree2,3)

	print(res)
	print(res2)
	print(res3)







