"""
You are given two non-empty linked lists representing two non-negative integers. The digits are 
stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

"""
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Input: l1 = [0], l2 = [0]
Output: [0]

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""

node = ListNode()

temp1 = l1
temp2 = l2


carry = 0 
sum = 0

while temp1 and temp2 :

	#add 




"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution:
	def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
		"""
		The function to add the value of the two lists 
		passes leetcode
		"""

		#make a new node 
		node = ListNode()
		head = node

		#make vars 
		carry, sum = 0,0

		#make the ptr
		temp1 , temp2 = l1,l2

		while temp1 and temp2 :

			#get the sum 
			sum = temp1.val + temp2.val + carry

			digit = sum % 10 
			carry = sum // 10 

			node.next = ListNode(digit)

			temp1 = temp1.next
			temp2 = temp2.next

			node = node.next
		
		#add the remaining

		while temp1:
			sum = temp1.val + carry
			carry = sum // 10
			val = sum % 10
			node.next = ListNode(val)
			node = node.next
			temp1 = temp1.next


		while temp2:
			sum = temp2.val + carry
			carry = sum // 10
			val = sum % 10
			node.next = ListNode(val)
			node = node.next
			temp2 = temp2.next

		  
		if carry != 0:
			carry_node = ListNode(carry)
			node.next = carry_node
		

		return head.next

		
		


