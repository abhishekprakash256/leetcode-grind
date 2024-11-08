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
length = 5 

curr_len = 5 - 2 - 1 

if curr.next:
    temp = curr.next
else:
    temp = None
    
[3,4,5]

curr.next = temp.next
temp.next = None

if n = 1 :




"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        The function to remove the nth node from the last 
        """

        #base case :
        if not head.next and n == 1:
            return None
        

        #get the length 
        curr = head
        length = 1 

        while curr:

            curr = curr.next
            length += 1

        
        #get the prev node pos 
        length_prev = length - (n)

        #set ptr
        ptr = head
        i = 0

        #star the removal loop 
        while i < length_prev:

            ptr = ptr.next
            i += 1 
        

        #remove the node 
        temp = ptr.next

        if temp.next :

            ptr.next = temp.next
        
        else:

            ptr.next = None
        
        temp.next = None
        







