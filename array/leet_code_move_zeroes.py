"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

"""


#test cases

nums = [0,1,2,0]
out = [1,2,0,0]


nums2 = [1,1,0,0,0,0,0]
out2 = [1,1,0,0,0,0,0]

nums3 = [0]
out3 = [0]

nums4 = [2,2,2]
out4 = [2,2,2]


nums5 = [0,0,0]
out5 = [0,0,0]

nums6 = [1,0,0,0,1]
out6 = [1,1,0,0,0]

nums7 = [1,1,1,0,1]
out = [1,1,1,0]


class Solution(object):
	def moveZeroes_incorrect(self, nums):

		l,r = 0,0
		i = 0


		while True or l <= len(nums) -1 :

			if nums[i] == 0:
				l = i
				break
			i+=1


		for a in range(l,len(nums)):

			if nums[a] != 0:
				print(a)
				r = a
				break


		#do the swapping logic

		while r <= len(nums) - 1:

			nums[r] , nums[l] = nums[l] , nums[r]

			while nums[r] !=0 or r <= len(nums) -1:

				r+=1

			r +=1
			l +=1


		return nums





if __name__ == "__main__":

	sol = Solution()

	res = sol.moveZeroes(nums7)

	print(res)








