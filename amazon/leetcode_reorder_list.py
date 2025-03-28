"""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
"""


"""

Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
 

Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
"""


"""


approach -- 

we can't go back 

value can be chnaged 

apped in a stack 

and a queue

[1,2,3,4]

[1,2,3,4]

first que element then pop 

1-4-2-3

we make two copy 

put in stack 

put in queue

when value are same we changed 

pop(0)

pop()





1->2->3->4->5

1->2->3<-4<-5

1->5->2->4->3


find mid point

rev the linking for the last half 

keep the pointer in the last and first 

then combine alernatively



"""


class Solution_wrong:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        #constraint case 
        if head.next is None :

            return None

        #make the stack and queue
        stack = []
        queue = []

        #ptr
        temp = head

        #append in the stack
        while temp :

            stack.append(temp)

            temp = temp.next

        #ptr
        temp = head

        #append in the stack
        while temp :

            queue.append(temp)

            temp = temp.next

        #make the new list

        temp = head

        node1, node2 = queue[0], stack[-1]

        count = 1

        while node1.val != node2.val :


            if count % 2 == 0 :

                node1 = queue.pop(0)

                temp.val = node1.val

            else :

                node2 = stack.pop()

                temp.val = node2.val

            count += 1

        return None



"""
1->2->3->4->5

1->2->3<-4<-5

1->5->2->4->3


"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution():
    """
    passes leetcode
    """

    def reorderList(self,head) -> None :
        """
        The function to reveres the list 
        """

        #constraint case of 0 node , 1 node , 2 node 
        if not head or not head.next or not head.next.next : 

            return None 

        #make the ptrs 
        slow , fast = head , head

        #find the mid point
        while fast and fast.next :

            slow = slow.next
            fast = fast.next.next

        
        #ptrs and divide the list in half
        curr = slow.next
        slow.next = None


        #rev the linking of the last half 
        prev = None 
        while curr :

            nxt_node = curr.next

            curr.next = prev

            prev = curr

            curr = nxt_node

        #ptrs
        temp1 = head
        temp2 = prev

        #combine two the halves
        while temp1 and temp2:

            nxt_node1 , nxt_node2 = temp1.next , temp2.next

            temp1.next = temp2

            if nxt_node1 :

                temp2.next = nxt_node1

            temp1 , temp2 =  nxt_node1, nxt_node2

        return None

























