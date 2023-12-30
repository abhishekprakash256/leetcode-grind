"""
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
"""


#import 
import linked_list


class Solution(object):
	def isPalindrome_brute_force(self, head):
		"""
		:type head: ListNode
		:rtype: bool
		"""

		#cover the edge case

		#no or single node 

		temp = head
		lst = []

		if temp is None or temp.next is None:

			return True

		
		#append in the list 
		while temp:

			lst.append(temp.val)
			temp = temp.next



		left , right = 0, len(lst) - 1

		#check the pallindrome logic

		while left <= right : 

			if lst[left] != lst[right] : 

				return False

			left +=1
			right -=1

		return True





if __name__ == "__main__":
	
	sol = Solution()
	help_fun = linked_list.Helper()

	res = sol.isPalindrome_brute_force(linked_list.head4)

	print(res)