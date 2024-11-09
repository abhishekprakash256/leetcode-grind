"""
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list. Return the linked list sorted as well.

"""

"""
if not head:
	return None 


if not head.next :

	return head


curr = head 

while curr :

	if curr.val == curr.next.val :
		
		curr.next = curr.next.next
	
	else:
	
		curr = curr.next



"""

class Solution:
	def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
		"""
		The function to remove the duplicate node
		"""

		#base case 
		if not head :
			return None 

		if head.next is None:
			return head
		

		#make the ptr 
		curr = head

		#start the removal loop 

		while curr and curr.next: 


			if curr.val == curr.next.val :

				curr.next = curr.next.next

			else:

				curr = curr.next


		return head








