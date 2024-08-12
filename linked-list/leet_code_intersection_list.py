"""
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

"""


"""
apprach 

-----------------

1. make two pointer 
2. check if two are equal and the exit if found 
3. increase them togther 

"""



class Solution:
	def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
		"""
		The function to find if two nodes are shared in the two linked list

		"""

		ptr_a = headA
		ptr_b = headB

		#star the loop for equal

		while ptr_a != ptr_b:

			if ptr_a:
				ptr_a = ptr_a.next

			else:
				ptr_a = headB


			if ptr_b:
				ptr_b = ptr_b.next


			else:
				ptr_b = headA


		return ptr_a



