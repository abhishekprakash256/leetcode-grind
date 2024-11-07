"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 
"""


"""

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]



[1,2,4]

[1,5,6]


"""

"""

merging algo -- 


#make two pointer 

temp1 = head1
temp2 = head2


#start the loop

while temp1 and temp2 :

	#both are equal :

	if temp1.val == temp2.val :

		temp3 = temp1
		temp3.next = temp2

		temp1 = temp1.next
		temp2 = temp2.next


	elif temp1.val < temp2.val :

		temp3 = temp1
		temp3.next = temp1


		temp1 = temp1.next

	else:

		temp3 = temp2
		temp3.next = temp2


		temp2 = temp2.next		




if temp2 :

	temp1.next = temp2


if temp1:

	temp2.next = temp1




"""





# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def mergeTwoLists(self, list1,list2):
		"""
		The function to merge the two lists
		"""


		#make the two ptrs 
		temp1 = list1
		temp2 = list2 


		#make a node 
		dummy = Listnode()


		#start the loop 

		while temp1 and temp2:

			#both are equal 

			if temp1.val == temp2.val :

				node = ListNode(temp2.val)

				node = node.next
				node = node.next

				temp1 = temp1.next
				temp2 = temp2.next

			elif temp1.val > temp2.val :

				node = ListNode(temp2.val)

				node = node.next

				temp2 = temp2.next


			else:

				node = ListNode(temp1.val)

				node = node.next

				temp1 = temp1.next

		return dummy.next











		




























