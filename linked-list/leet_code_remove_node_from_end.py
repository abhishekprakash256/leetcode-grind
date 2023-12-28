"""
remove the nth node from the end of the linked list 
"""

import linked_list



class Solution():
	def removeNthFromEnd(self,head,n: int) :
		"""
		The function to remove the nth node from the back of the list 
		"""


		#temp ptr
		first, last = head,head
		count = 0

		while count !=n:
			
			count +=1
			last = last.next


		while True:

			if last.next is None:
				
				print(first.val)
				#node delete logic
				temp_node = first.next

				print(temp_node.val) 
				first.val = temp_node.val

				print(first.val)
				first.next = temp_node.next
				temp_node.next = None
				del(temp_node)
				break

			last = last.next
			first = first.next
		

if __name__ == "__main__":
	sol = Solution()

	sol.removeNthFromEnd(linked_list.head,1)

	help_fun = linked_list.Helper()

	help_fun.printTree(linked_list.head)


			



			



			

