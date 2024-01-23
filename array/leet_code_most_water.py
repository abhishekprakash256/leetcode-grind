"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.
"""

"""
Approaches 

-- 
it's a list with each next iter as one area 
brute force approach = 

two loops - 
	- start from the initia to end 
	- keep the max area after every calculation 
	- update the max area as per iteration 

return the max area 


optmization of the problem - 

use the two pointer 
or we can start either the edges or middle 

if we start edges - 
	- what is the condition to move ? 

if we start the middle - 
	- what is condition to move ? 

if we start like a window apporach 
	- what is condtion to slide 


edge cases -

 - one return none

---
start with the slide window two pointer 
keep a queue always decreasing 

initilization

- left = 0 ,right = left +1
- move the pointer 
	- move the left and right pointer 
	- if right find grater value than left , move the pointer to that 
	- start the iteration 
- area calculation mechanism with max tracking 


"""


#test cases ----- 
nums = [1,8,6,2,5,4,8,3,7]
out = 49 

nums2 = [1,1,1,1,1]
out2 = 4 


nums3 = [1,1,100,100, 3]
out3 = 100

#edge cases 
nums4 = [1]
out4 = 0 

nums5 = []
out5 = 0 


class Solution():

	def maxArea(self,nums) : 
		"""
		Find the max area that can hold water inside the lists 
		"""

		#cover the edge cases 
		if len(nums) <= 1:
			return 0 

		#initilaization of the pointers 
		left = 0 
		right = left + 1 
		area = 0 

		#start the sliding window approach 

		while right < len(nums):

			temp_area = (nums[right] - nums[left])* (right - left)
			area = max(temp_area,area)

			if nums[right] > nums[left]:
				left, right = right, right + 1

			elif nums[right] <= nums[left] : 
				right +=1

		return area 










