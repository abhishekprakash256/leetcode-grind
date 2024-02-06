"""
add the two numbers from the linked list 
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

"""


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


#make the first list 

head1 = ListNode(2)
node12 = ListNode(4)
node13 = ListNode(3)

#connect the linked list 
head1.next = node12
node12.next = node13


#make the second linked list 

head2 = ListNode(5)
node22 = ListNode(6)
node23 = ListNode(4)

#connect the linked list 
head2.next = node22
node22.next = node23


#make the third list 
head3 = ListNode(1)

head32 = ListNode(9)

#connect the list 



#make the 4 list 

head4 = ListNode(9)
node42 = ListNode(9)
node43 = ListNode(9)


#connect the list
head4.next = node42
node42.next = node43

#make the second list
head5 = ListNode(9)
node52= ListNode(9)
node53 = ListNode(7)
node54 = ListNode(6)

#connect the connect 
head5.next = node52
node52.next = node53
node53.next = node54




class Solution():

	def printList(self,node):
		
		temp = node
		while temp:

			print(temp.val)
			temp = temp.next



	def addTwoNumbers(self,l1, l2):
		"""
		the function to find the sum of the two nodes
		"""

		dummy = ListNode()
		carry = 0 
		cur = dummy
		temp_sum = 0 

		while l1 and l2:

			temp_sum = l1.val + l2.val + carry

			#carry logic
			carry = temp_sum // 10 
			val = temp_sum % 10 

			cur.next = ListNode(val)

			cur = cur.next

			l1 = l1.next
			l2 = l2.next


		if carry !=0 :
			carry_node = ListNode(carry)
			cur.next = carry_node

		if l1: 
			cur.next = l1


		if l2:
			cur.next = l2

		return dummy.next

		self.printList(dummy.next)

		"""
		temp = dummy.next

		while temp:

			print(temp.val)
			temp = temp.next

		"""


if __name__ == '__main__':
	sol = Solution()

	#sol.printList(head1)

	res = sol.addTwoNumbers(head1,head2)

	print(res)