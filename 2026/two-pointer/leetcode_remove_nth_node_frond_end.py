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




class Solution:
	def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
		"""
		The function to remove the nth node from the start
		"""

		#constaint case 
		


