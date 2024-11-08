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
        if not head.next :
            return None
        

        #get the length 
        length = 1

        #make the ptr 
        cur = head
        
        #calc the length
        while curr:

            length += 1 
            curr = curr.next

        
        #if the node is head 
        if length - n == 0:

            temp = head.next
            head.next = None

            return temp


        #if remove the last node
        if n == 1:

            temp = head

            while True:

                if temp.next:

                    temp = temp.next
                
                else:

                    temp.next = None
                    return head
            

        #case if not last and first node 

        #get the length 
        pre_len = length - n
        prev = head
        i = 1

        while i < pre_len :

            prev = prev.next
        
        prev.next = prev.next.next


        return head










        

        

        







