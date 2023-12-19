# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.



#print(21%10) #1
#print(21//10) #2



lst = [1,2,3]
lst2 = [4,5,6]

lst3 = [9,9]
lst4 = [9,9,9,9,9,9]

lst5 = [0]
lst6 = [0]

class Solution():

	def sum_two_num(self,arr,arr2):
		"""
		make the program to add two list and have the carry feature as well
		"""

		#make the arr as always than arr2
		#arr will be shorter array always

		if len(arr) > len(arr2):

			arr, arr2 = arr2, arr


		for x in range(len(arr2) - len(arr)):

			#make the array equal
			arr.insert(0,0)


		sum_arr = []
		carry, i,j =  0 ,len(arr) - 1, len(arr) - 1

		while i >= 0 :

			print(i)

			val = carry + arr[i] + arr2[j]
			
			# the carry computation	
			lst_val = val % 10
			carry = val // 10 
			sum_arr.insert(0,lst_val)
			
			#decrease pointer
			i -=1
			j -=1


		if carry:

			sum_arr.insert(0,carry)


		return sum_arr




if __name__== "__main__":

	sol = Solution()
	res = sol.sum_two_num(lst3,lst4)


	print(res)




	
	

		
			
		
		
		
		
		
		
	
