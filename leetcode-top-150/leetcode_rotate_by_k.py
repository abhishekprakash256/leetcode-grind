"""
Given the head of a linked list, rotate the list to the right by k places.
"""


"""
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Input: head = [0,1,2], k = 4
Output: [2,0,1]
"""


"""
algo - 
use two pointer 

one at head 
other at length - k 


#base case 
if not head:
    return None 

if not head.next:
    return node

length = 1 

temp = head 

while temp:
    length += 1
    temp = temp.next


if k < lenghth :
    second_ptr_pos = length - pos 

else:

    second_ptr_pos = length - (length//k)

    
r = head 

for i in range(second_ptr):

    r = r.next

tail = head 

#make to the last 
while tail.next : 

    tail = tail.next 

#sawp the nodes 

tail.next = head 
secon_ptr_pos.next = None 



"""

from typing import Optional , ListNode

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        """
        The function to rotate the linked list by k times 
        """

        #base case 
        if not head :
            return None 

        if not head.next : 
            return head 
        

        #get the length 
        length = 1 
        temp = head 

        while temp:

            length += 1 
            temp = temp.next

        #get the second ptr pos 

        if k < length:

            r = length - k 
        
        else:

            r = length - (length//k)

        
        #get the last node 
        right = head 

        while right.next:

            right = right.next
        

        #put the seond ptr in pos 

        left = head

        for _ in range(length-r ):

            left = left.next

        
        #swap the nodes

        left.next = None 
        right.next = head

        return head
        


        




            
