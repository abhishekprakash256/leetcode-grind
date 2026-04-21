"""
The question to reverse the link list 
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


#print the list

"""
curr = head

while curr:

	print(curr.val)

	curr = curr.next
"""

"""
approch -->

1->2->3->4->5

1<-2<-3<-4<-5

dummy->1->2->3->4->5

dummy.next = head

curr = head

prev = curr

while curr:

temp = curr.next

curr.next = prev

prev = curr

curr = temp



"""

class LinkListHelper():

	def print_link_list(self,head):

		curr = head

		while curr :

			print(curr.val)

			curr = curr.next



	def reverse_link_list(self,head):
		"""
		reverse the linked list
		"""

		#make the ptrs
		curr = head

		prev = None

		#reverse the list
		while curr:

			temp = curr.next

			curr.next = prev

			prev = curr

			curr = temp

		return prev

		




link_list_helper = LinkListHelper()

#link_list_helper.print_link_list(head)

link_list_helper.reverse_link_list(head)

link_list_helper.print_link_list(node_5)