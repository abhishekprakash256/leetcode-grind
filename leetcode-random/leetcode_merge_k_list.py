"""
You are given an array of k linked-lists lists, each linked-list is sorted in 

ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
"""



"""

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]

merging them into one sorted list:
1->1->2->3->4->4->5->6


Example 2:
Input: lists = []
Output: []
Example 3:

"""

"""
approach -- 

merge two list and then merge other list ? 

keep on merging as we traverse ? 


two loops , outer and inner 

1->4->5
1->3->4

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


dummy = listNode()
curr = dummy

for i in range(1,lists) :

	left = lists[i-1]
	right = lists[i]

	l, r = left[0] , right[0]

	while l and r :

		if l.val < r.val :

			curr.next = l
			l = r.next

		else:

			curr.next = r
			l = r.next

		curr = curr.next

	if l:
		curr.next = l

	elif r:
		curr.next = r


"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
		"""
		The function to merge the k lists 
		"""

		if len(lists) == 1 :

			return lists[0]


		#make the dummy node
		dummy = ListNode()
		curr = dummy


		#start the traversal

		for i in range(1,len(lists)) :

			l = lists[i-1]
			r = lists[i]

			while l and r :

				if l.val < r.val :

					curr.next = l
					l = l.next

				else:

					curr.next = r 
					r = r.next

				curr = curr.next

			if l :

				curr.next = l

			elif r :

				curr.next = r


		return dummy.next



		