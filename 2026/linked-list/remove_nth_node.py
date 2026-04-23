"""
remove the nth node from the linked list
"""

class Node():

	def __init__(self,val):

		self.val = val
		self.next = None




#make the list

head = Node(1)

node_2 = Node(2)

node_3 = Node(3)

node_4 = Node(4)

node_5 = Node(5)


head.next = node_2

node_2.next = node_3

node_3.next = node_4

node_4.next = node_5




class LinkedListHelper():


	def remove_nth_node_end(self, head , n ):
		"""
		The function to remove the nth node
		"""

		dummy = Node(None)

		dummy.next = head


		fast = dummy
		slow = dummy

		#put the nth node to nth pos
		for i in range(n+1) :

			fast = fast.next


		#take to the nth node
		while fast :

			fast = fast.next
			slow = slow.next


		#delete the node
		slow.next = slow.next.next

		return dummy.next



	def print_link_list(self,head):

		curr = head

		while curr :

			print(curr.val)

			curr = curr.next




if __name__ == "__main__" :


	linkedlisthelper = LinkedListHelper()

	print(linkedlisthelper.print_link_list(head))


	linkedlisthelper.remove_nth_node_end(head, 3)


	print(linkedlisthelper.print_link_list(head))






















