"""
Reverse Linked List
"""
#imports the list 
import linked_list



class Solution:
	def reverseList(self, head):
		"""
		Reverese the linked list 
		using the brute force approach
		"""

		#edge case 2 - empty
		if head is None:
			return head

		#edge case 1 - only head
		if head.next is None:
			return head
	


		lst = []
		temp = head

		#append the values in the list 
		while True:

			lst.append(temp.val)

			if temp.next is None:
				break

			temp = temp.next
		
		#reverse the list 
		lst.reverse()

		i = 0 
		temp = head

		while True:
			
			temp.val = lst[i]
			temp = temp.next
			i +=1

			if temp.next is None:
				temp.val = lst[i]
				break

		return head





if __name__ == "__main__":
	sol = Solution()
	help_fun = linked_list.Helper()


	sol.reverseList(linked_list.head)
	help_fun.printTree(linked_list.head)




		
		



