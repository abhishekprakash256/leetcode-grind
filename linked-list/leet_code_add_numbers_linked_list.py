"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""


"""
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]



"""



"""
approach 

----

left = head1
right = head2


sum = 0 
carry = 0

dummy_node = ListNode()
start_node = dummy_node

while left or right:
	
	cur_sum = left.val + right.val
	val = cur_sum // 10
	carry = cur_sum % 10
	new_node = ListNode(val)
	dummy_node.next = new_node



if left:
	
	dummy_node.next = left


if right:
	dummy_node.next = right


return start_node.next





"""

class Solution:
    def addTwoNumbers(self, head1: ListNode, head2: ListNode) -> ListNode:

    	"""
		The soln passed leet code and accepted
    	"""
        left = head1
        right = head2

        carry = 0
        dummy_node = ListNode(0)
        start_node = dummy_node

        while left or right or carry:
            # Get the values for the current nodes, or 0 if the node is None
            val1 = left.val if left else 0
            val2 = right.val if right else 0

            # Calculate the sum and the carry
            cur_sum = val1 + val2 + carry
            carry = cur_sum // 10
            val = cur_sum % 10

            # Create a new node with the calculated value and move the dummy_node pointer
            new_node = ListNode(val)
            dummy_node.next = new_node
            dummy_node = dummy_node.next

            # Move the pointers for left and right if they are not None
            if left:
                left = left.next
            if right:
                right = right.next

        # Return the result list, skipping the dummy node
        return start_node.next
