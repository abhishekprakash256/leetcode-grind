"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing 
together the nodes of the first two lists.

Return the head of the merged linked list.
"""


"""


"""

class ListNode():

	def __init__(self,val,next = None):

		self.val = val
		self.next = next


root1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

root1.next = node2
node2.next = node3
node3.next = node4

root2 = ListNode(1)
node5 = ListNode(5)
node6 = ListNode(6)

root2.next = node5
node5.next = node6


def print_list(node):

	while node:

		print(node.val)

		node = node.next


def print_list2(node):

	temp = node

	while temp :

		print(temp.val)

		temp = temp.next

print(print_list(root1))

print(print_list(root2))

print(print_list2(root1))

print(print_list2(root2))




class Solution():

	def mergeTwoLists(self,node1,node2) :
		"""
		The function to merge the two sorted lists
		"""

		#constraint case

		#no node cases
		if not node1 and node2:

			return None 

		if not node1:

			return node2

		if not node2 :

			return node1

		#make the dummy node 
		dummy = ListNode(0)

		curr = dummy

		while node1 and node2 :

			if node1.val < node2.val :

				curr.next = node1

				node1 = node1.next

			else :

				curr.next = node2

				node2 = node2.next

			curr = curr.next  # Move forward

		#merge the remain 
		if node1 :

			curr.next = node1

		if node2 :

			curr.next = node2

		return dummy.next



sol = Solution()

res = sol.mergeTwoLists(root1,root2)

print(print_list2(res))