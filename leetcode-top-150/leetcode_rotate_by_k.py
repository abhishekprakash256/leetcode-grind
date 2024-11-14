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

class Node:
    def __init__(self,val=None,next = None ):
        self.val = val
        self.next = next



#make the node

head = Node(1)
node1 = Node(2)
node2 = Node(3)
node3 = Node(4)
node4 = Node(5)

#connect the linked list 
head.next = node1
node1.next = node2
node2.next = node3
node3.next = node4




class Helper_fun:
    
    def print_list(self,head):
        """
        To print the list
        """

        curr = head

        while curr:

            print(curr.val)
            curr = curr.next







class Solution:
    def rotateRight(self, head, k: int):
        """
        Rotates the linked list to the right by k places.
        passes leet code
        """

        # Base case: if the list is empty or has only one element
        if not head or not head.next:
            return head

        # Calculate the length of the list
        length = 0
        temp = head

        while temp:
            length += 1
            temp = temp.next

        # Optimize k to avoid unnecessary rotations
        k = k % length
        if k == 0:
            return head  # No rotation needed

        # Find the new tail (length - k - 1) and new head (length - k)
        new_tail_pos = length - k - 1
        new_tail = head
        for _ in range(new_tail_pos):
            new_tail = new_tail.next

        new_head = new_tail.next  # New head is next of new_tail

        # Find the last node to connect it with the original head
        temp = new_head
        while temp.next:
            temp = temp.next
        temp.next = head  # Connect last node to the original head

        # Break the list at new_tail
        new_tail.next = None

        return new_head


        



helper_fun = Helper_fun()

sol =  Solution()

#print(helper_fun.print_list(head))

sol.rotateRight(head,2)

print(helper_fun.print_list(head))

            
