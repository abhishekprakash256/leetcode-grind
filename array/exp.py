lst = [1,2,3,4,5,6,7,8]

lst2 =['a','b','c']


"""

for i in range(len(lst2)):

	print(i,lst2[i])


for i,a in enumerate(lst2):

	print(i,a)

"""

def rotate(nums):

	length = len(nums)
	r = length - 1

	for i in range(length // 2):

		print(i ,r )

		nums[i] , nums[r] = nums[r] , nums[i]
		r -= 1

	return nums


def rotate2(nums):

	length = len(nums)
	r = length - 1
	l = 0 


	while l < r:

		nums[l] , nums[r] = nums[r] , nums[l]

		r -= 1 
		l += 1

	



print(rotate(lst))
