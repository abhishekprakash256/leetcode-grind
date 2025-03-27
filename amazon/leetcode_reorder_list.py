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




class Solution():

    def reorderList(self,head) -> None :
        """
        The function to reveres the list 
        """

        #constrraint case 
        if not node or not node.next or node.next.next:

            return None


        #make the ptrs 
        fast , slow = head , head

        while fast.next or fast :

            slow = slow.next 
            fast = fast.next.next


        #from the middle rev the list
        




