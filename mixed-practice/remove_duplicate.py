"""
remove the duplicate from the array 
"""

#test cases 
test = [1,2,4,5,7,7,7]
out = [1,2,4,5,7]


#test case 2 
test2 = [1,1,1,1,1]
out = [1]


#test case 3 
test3 = [1,2,2,2,3,3,3]
out3 = [1,2,3]



"""
two pointe approach 

l = 0 
r = l + 1 

star my loop 
cond =  r < len(list)

if lst[l] == lst[r]:

	temp = r 
	#advance pointer
	r = temp + 1
	l +=1
	lst.remove(temp)

else:
	l+=1
	r+=1

"""

class Solution():
	def removeDuplicates(self,nums):
		"""
		the function to remove the duplicate and add "_" in the place 
		"""
		#edge case of less than 1 length
		if len(nums) <= 1 :
			return len(nums)
		
		#initialize the pointers 
		l = 0 
		r = l + 1

		#start the loop 
		while r < len(nums):
			
			if nums[l] == nums[r]:
				nums.pop(l)
			

			else:
				r +=1
				l +=1
		
		return len(nums)


res = removeDuplicate(test2)
print(res)






	
	
