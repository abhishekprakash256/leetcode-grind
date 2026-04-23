"""
Merge the sorted linked list
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



head_2 = Node(3)

node_6 = Node(4)

node_7 = Node(7)

#connect the list

head_2.next = node_6

node_6.next = node_7



class LinkedListHelper():

	def merge_node(self, l1, l2) :
		"""
		The functtion to merge the linked list
		"""

		dummy = Node(None)

		curr = dummy

		#merge the node 
		while l1 and l2 :

			if l1.val < l2.val :

				curr.next = l1

				l1 = l1.next

			else :

				curr.next = l2

				l2 = l2.next

			curr = curr.next


		#attach the remainig 
		if l1 :

			curr.next = l1

		if l2 :

			curr.next = l2

		return dummy.next



	def print_link_list(self,head):

		curr = head

		while curr :

			print(curr.val)

			curr = curr.next





if __name__ == "__main__" :


	linkedlisthelper = LinkedListHelper()

	print(linkedlisthelper.print_link_list(head))


	print(linkedlisthelper.print_link_list(head_2))


	res = linkedlisthelper.merge_node(head, head_2)

	print(linkedlisthelper.print_link_list(res))










				





		