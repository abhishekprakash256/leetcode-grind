"""
Reverse Linked List
"""
#imports the list 
import linked_list



class Solution:
	def reverseList_brute_force(self, head):
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
	

	def reverseList(self, head):
		"""
		The function reverese the linked list 
		"""
		prev = None
		curr = head

		while curr:
			#reverse logic 
			next_temp = curr.next
			curr.next = prev
			prev = curr
			curr = next_temp
			
		return prev





if __name__ == "__main__":
	sol = Solution()
	help_fun = linked_list.Helper()


	sol.reverseList_brute_force(linked_list.head)
	help_fun.printTree(linked_list.head)




		
		



