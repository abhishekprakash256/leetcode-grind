"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]



"""



"""
the soln 

--

head = [1,2,3,4,5]

1->2->3->4->5

5->4->3->2->1

brute force 

#edge case 
temp = root

if not temp :

	retun []


1. append all in a list 
2 rev that list 
3. make a new list by iteration and keep adding elemnts 

O(n), O(n)


optimal soln -  

1. 



"""




# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next




class Solution:
	def reverseList(self, head: Optional[ListNode]):
		"""
		Rewverse the link list
		works and passed on leetcode

		"""
		#base case

		if not head:
			return None

		prev = None
		curr = head

		while curr:

			#swap the pointers 
			next_node = curr.next
			curr.next = prev
			prev = curr
			curr = next_node

		return prev

























