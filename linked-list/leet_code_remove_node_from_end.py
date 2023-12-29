"""
remove the nth node from the end of the linked list 
"""

import linked_list


# the code is not working 
class Solution():
	def removeNthFromEnd(self,head,n: int) :
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
		

if __name__ == "__main__":
	sol = Solution()

	"""

	sol.removeNthFromEnd(linked_list.head,2)

	help_fun = linked_list.Helper()

	help_fun.printTree(linked_list.head)
	"""

	sol.removeNthFromEnd(linked_list.head2,1)

			



			



			

