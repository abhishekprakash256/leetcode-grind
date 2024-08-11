"""

Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Input: head = [1,2,2,1]
Output: true


Input: head = [1,2]
Output: false

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9

"""





"""
brute force 

1. append in a list
2. and check if the list is pallindrome
3. return true or false based

---------------

1. rev the list 
2. match the list with second one
3. return true if correct


---------------
1. find the half of the linked list 
2. Reverse half of the link list 
3. match the half and other half of the list





"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def isPalindrome(self, head: Optional[ListNode]) -> bool:
		"""
		The function to find the plalindrome of the link list
		The code passes leetcode 
		"""

		#find the mid 	
		slow = head 
		fast = head

		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next


		#reverse the list 

		prev = None
		curr = slow

		while curr:

			#swap the pointers 
			next_node = curr.next
			curr.next = prev
			prev = curr
			curr = next_node



		#check if both are equal

		left = head
		right = prev

		while right:

			if left.val != right.val:

				return False

			left = left.next
			right = right.next


		return True








