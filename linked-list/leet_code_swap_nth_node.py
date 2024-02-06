"""
Return the head of the linked list after swapping 
the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).
"""

"""
The edge case 
#len list is one 
return head

inp---
head
k

-------
l = head
l_counter = 0
r = head
r_counter = 0 
temp = head
length = 0 

#find length 

while temp:
    
    length +=1
    temp = temp.next


while l_counter != k :

    l = l.next


while r_counter != (length - k ):

    r = r.next


#sawp logic 
l.val , r.val = r.val, l.val 

return head


"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        function to swap the nth nodes
        """ 
        #edge case of one node 
        if head.next is None:
            return head

        #initilaization of vars
        temp, l, r = head, head, head
        length = 1 
        l_counter = 1
        r_counter = 1 

        #calc the length 
        while temp:
            length +=1
            temp = temp.next

        #reacth the nth start node
        while l_counter != k:
            l_counter +=1
            l = l.next

        #reach the nth node from last 
        while r_counter != (length - k ):
            r_counter +=1
            r = r.next
        
        print(l.val,r.val)
        #swap the nodes
        l.val, r.val = r.val , l.val

        return head
        


