class Node():
	def __init__(self,val):
		self.val = val
		self.next = None


#make the list 

head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)


#connect the linked list 
head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


#make a single list 
head2 = Node(5)


#make the list 
head3 = Node(1)
node6 = Node(2)

#connect the list 
head3.next = node6


#make the pallindrome list 
head4 = Node(1)
node7 = Node(2)
node8 = Node(1)

#vconnect the node
head4.next = node7
node7.next = node8


class Helper():
	
	def printList(self,head):
		"""
		The function to print the tree 
		"""
		temp = head

		while True:

			print(temp.val)

			if temp.next is None:
				break
		
			temp = temp.next

