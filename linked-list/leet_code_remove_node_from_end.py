"""
remove the nth node from the end of the linked list 
"""

import linked_list


# the code is not working 
class Solution():
	def removeNthFromEnd_incorrect(self,head,n: int) :
		"""
		The function to remove the nth node from the back of the list 
		"""


		#temp ptr
		first, last = head,head
		count = 0


		#handling the exception of one node
		if last.next is None and first.next is None:
			return None

		while count !=n:
			
			count +=1
			last = last.next

		while True:

			if last.next is None:
				
				#node delete logic
				temp = first.next
				first.next = temp.next
				temp.next = None
				break

			last = last.next
			first = first.next

		return head

	def removeNthFromEnd(self,head,n: int) :
		"""
		The function to remove the nth node from the back of the list 
		"""

		#temp ptr
		first, last = head,head
		count = 1


		#handling the exception of one node
		if last.next is None and first.next is None:
			return None

		while count !=n:
			
			count +=1
			last = last.next
		

		while True:

			#node breakig logic 
			if last.next is None:
				
				#delete the node in place 
				temp_node = first.next 
				first.val = temp_node.val
				first.next = temp_node.next
				temp_node.next = None
				del(temp_node)
				break


			last = last.next
			first = first.next 

		return head



		

if __name__ == "__main__":
	sol = Solution()

	"""

	sol.removeNthFromEnd(linked_list.head,2)

	

	help_fun.printTree(linked_list.head)
	"""

	#sol.removeNthFromEnd(linked_list.head2,1)

	help_fun = linked_list.Helper()

	sol.removeNthFromEnd(linked_list.head,2)
	help_fun.printTree(linked_list.head)

	#sol.removeNthFromEnd(linked_list.head2,0)

	#sol.removeNthFromEnd(linked_list.head3,2)	





			



			

