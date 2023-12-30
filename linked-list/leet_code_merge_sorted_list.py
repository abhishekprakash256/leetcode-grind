"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""
import linked_list

class Solution:
	def mergeTwoLists(self, head, head2):
		"""
		The function to merge the two linked list that are sorted
		"""

		#make the dummy node 
		dummy = linked_list.Node(0)
		curr = dummy

		while head and head2:

			if head.val < head2.val:

				curr.next = head
				head = head.next 

			else:

				curr.next = head2
				head2 = head2.next

			curr = curr.next


		if head:

			curr.next = head

		else:

			curr.next = head2


		return dummy.next







if __name__ == "__main__":

	sol = Solution()

	sol.mergeTwoLists(linked_list.head,linked_list.head2)


