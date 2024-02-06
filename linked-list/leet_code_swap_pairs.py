"""

Given a linked list, swap every two adjacent nodes and return its head. 
You must solve the problem without modifying the values in the list's nodes 
(i.e., only nodes themselves may be changed.)


constraint is no node 
constraint is 1 node 


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
 
"""



"""
[1,3]

swap before

if r.next is None :
	break

if r.next.next is None:
	break

l = l.next.next
r = r.next.next

[1,2,3]


[1,2,3,5]


Algo -- 

#edge case 

#is no node 
if not node:
	return None 

#is only one node
if node.next is None:
	return node


#the soln two pointer 
l = head
r = head.next

#start my loop 

while 
	

return head

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
		"""
		function to swap the pointers
		"""

		#edge case coverage
		if not head:
			return None
		
		if head.next is None:
			return head
		
		#initilaize the vars
		l = head
		r = head.next

		while True:

			l.val, r.val = r.val, l.val

			if r.next is None:
				break
			
			elif r.next.next is None :
				break
			
			l = l.next.next
			r = r.next.next
			

		
		return head


class Solution2:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while prev.next and prev.next.next:
            first_node = prev.next
            second_node = prev.next.next
            
            # Swapping the nodes
            first_node.next = second_node.next
            second_node.next = first_node
            prev.next = second_node
            
            # Move to the next pair
            prev = first_node
        
        return dummy.next

		