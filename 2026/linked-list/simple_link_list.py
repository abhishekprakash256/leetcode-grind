"""
the implementation of a simple link list
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


curr = head

while curr:

	print(curr.val)

	curr = curr.next


