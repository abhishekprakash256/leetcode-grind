"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
"""

"""
nums = [2,0,2,1,1,0]
out = [0,0,1,1,2,2]


#
sort on place 

#
count the num on place by 3 pass algo 
0, 1, 2 

count0 = 0 

brute force 


count0, count1, count2 = 0,0,0

for i in nums:

	if i == 0: 
		count0 +=1

	elif i == 1:
		count1 +=1

	elif i == 2:
		count2 +=1


for i in range(count0):
	nums.pop(0)
	nums.append(0)

for j in range(count1):
	nums.pop(0)
	nums.append(1)

for k in range(count2):
	nums.pop(0)
	nums.append(2)


#the optim approach 

use three pointers 

start the pointers with 

i,m,r = 0, 0, len(nums) - 1 

condn 
 
[2,2,2,1,0]
 
[0,1,0,1,2]


[1,1,2,2,0]
[0,1,2,2,1]

if nums[m] == 0 or nums[r] == 0 : 
	nums[m] , nums[i] = nums[i] , nums[m]
	i +=1



elif nums[m] = 2 : 
	nums[m], nums[r] = nums[r] , nums[m]

	r -=1

m +=1
	

"""







class Solution2():

	def sortColors(self,nums):
		"""
		The function to find the number of zeros
		"""
		
		count0, count1, count2 = 0,0,0

		for i in nums:

			if i == 0: 
				count0 +=1

			elif i == 1:
				count1 +=1

			elif i == 2:
				count2 +=1


		for i in range(count0):
			nums.pop(0)
			nums.append(0)

		for j in range(count1):
			nums.pop(0)
			nums.append(1)

		for k in range(count2):
			nums.pop(0)
			nums.append(2)


		return nums


"""
The algo using the swaaping techniue 

use 3 pointers 

i,m,r = 0 ,0 , len(nums) -1 

#start the loop 

while m < r:

	if nums[m] == 0 : 
		nums[m], nums[i] = nums[i], nums[m]
		m+=1
		i+=1
	
	elif nums[m] == 2 :
		nums[m], nums[r] = nums[r], nums[m]
		m+=1
		r-=1

return nums


"""


nums = [2,0,2,1,1,0]
nums2 = [2,0,1]

class Solution():
	def sortColors(self,nums):
		"""
		To sort the colors in the nums 
		"""

		#vars 
		i ,m ,r = 0,0, len(nums) - 1

		#loop over 

		while m <= r : 

			if nums[m] == 0: 
				nums[m] , nums[i] = nums[i] , nums[m]
				i +=1
				m +=1

			elif nums[m] == 1:
				m += 1 

			elif nums[m] == 2 : 
				nums[m], nums[r] = nums[r] , nums[m]
				r -=1


		return nums


if __name__ == "__main__":
	sol = Solution()
	print(sol.sortColors(nums2))