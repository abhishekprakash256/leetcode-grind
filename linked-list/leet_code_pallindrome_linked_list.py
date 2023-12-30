"""
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
"""


#import 
import linked_list


class Solution(object):
	def isPalindrome(self, head):
		"""
		:type head: ListNode
		:rtype: bool
		"""

		#cover the edge case

		#no or single node 

		temp = head

		if temp is None or temp.next is None:

			return True



		#make the  