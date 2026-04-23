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

		