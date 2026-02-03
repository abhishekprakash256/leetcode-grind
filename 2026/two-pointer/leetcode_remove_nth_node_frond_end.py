"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""


"""

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]

"""


"""
Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

"""


"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


traveral is the key -->

two pointer one to the end and get the length 

the move the next pointer to length 

move = length - n 

remove the fron node

how to remove the node - 

edge case remove the last node 

one node

if last node just make before node next to node

removing will require temp 





"""

from typing import List , Optional


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next




class SolutionWrong:
	def removeNthFromEndWrong(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
		"""
		The function to remove the nth node from the start
		"""

		#length of list
		length = 0

		#ptrs
		temp = head

		#get the length list
		while temp :

			temp = temp.next

			length += 1	

		#constraint case
		if length == 1 and n == 1 :

			return None

		if length == 1 and n == 0:

			return head

		#ptrs
		prev = 0

		temp = head

		#case if n == 1 
		if n == 1:

			while prev <= ( length - 1 ) :

				 temp = temp.next

				 prev += 1

			#remove the node

			temp.next = None

			return head

		#not n == 1 

		while prev < ( length - n ):

			temp = temp.next

			prev += 1

		pass

		#remove the node







class SolutionWrong2:
	def removeNthFromEndWrong2(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
		"""
		The function to remove the nth node from the start
		"""

		#length var
		length = 0

		#ptrs
		temp = head

		#get the length
		while temp :

			length += 1 

			temp = temp.next


		#case by length 

		if length == 1 :

			return None

		if length == 2 :

			#remove the last node 

			if n == 1 :

				temp = head

				temp.next = None

				return head

			else :

				temp = head

				temp_head = temp.next

				temp.next = None 

				return temp_head


		#make ptrs 
		temp = head
		prev = 0

		#case for length 3 or greater 

		while prev < ( length - n ) :

			temp = temp.next

			prev += 1 


		#remove the node 
		temp_1 = temp.next

		pass





class Solution:
	def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
		"""
		The function to remove the nth node from the list
		"""

		#make the dummy node 
		dummy = ListNode() 

		#make the head
		dummy.next = head

		#make the ptrs
		slow , fast = dummy , dummy

		#move the fast pointer
		for _ in range(n+1) :

			fast = fast.next

		#move the slow pointer
		while fast :

			fast = fast.next

			slow = slow.next

		#remove the node
		slow.next = slow.next.next

		return dummy.next





		








