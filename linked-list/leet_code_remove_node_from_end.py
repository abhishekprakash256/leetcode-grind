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

	def removeNthFromEnd_incorrect2(self,head,n: int) :
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


	#correct verison 

	def removeNthFromEnd(self, head, n: int):
		"""
		The function to remove the nth node from the back of the list 
		"""

		# temp ptr
		first, last = head, head
		count = 1

		# Handling the exception of one node
		if last.next is None and first.next is None:
			return None

		# Move the 'last' pointer n nodes ahead
		while count != n:
			count += 1
			last = last.next

		# Create a dummy node to handle cases where the head is removed
		dummy = ListNode(0)
		dummy.next = head
		first = dummy

		# Move 'first' and 'last' pointers until 'last' reaches the end
		while last.next is not None:
			last = last.next
			first = first.next

		# Remove the nth node by updating 'first' pointer
		first.next = first.next.next

		# Return the updated head
		return dummy.next


		

if __name__ == "__main__":
	sol = Solution()

	"""

	sol.removeNthFromEnd(linked_list.head,2)

	

	help_fun.printTree(linked_list.head)
	"""

	#sol.removeNthFromEnd(linked_list.head2,1)

	help_fun = linked_list.Helper()

	#sol.removeNthFromEnd(linked_list.head,2)
	

	#sol.removeNthFromEnd(linked_list.head2,0)

	sol.removeNthFromEnd(linked_list.head3,1)	

	help_fun.printTree(linked_list.head3)





			



			

