"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. 
If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.


The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000
"""


"""
constarint is  -- 

leave the reamin node as given after the kth divide node is done 

swap without changing values 




edge case 
#one node
if node.next is None:
    return node



one helper func -- to swap values 

one to iter the list and divide in the zones of swapping 

#inp
head 
k 

-----

#if one node
    return head

first part ----
def helper(self,l,r):

    temp_r = r.next
    
    while l is not r :

        r.next = l.next
        l.next = temp_r

        l = l.next
        r = r.next


second part ---
def reverseKGroup(head,k)


#vars 
l= head
r = head 
temp = head 
count = 1 

#start the loop 
while temp:

    coutn +=1

    if count < k:
        r = r.next
    
    else:
        self.helper(l,r)
        count = 1
        l = r.next
        r = temp 
    
    temp = temp.next 

     













"""

