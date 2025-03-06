"""
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.
"""

"""
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]



0 <= n <= 1000
-104 <= Node.val <= 104
Node.random is null or is pointing to some node in the linked list.

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

"""

"""
approach -- 

constraints case 
if no pointer return none 

if one pointer retiurn the Node(node.val)


craete a hashmap 

make a node and create a copy of the node for mapper 

original_node : copy_node

attach the next and random node 

.next is the node.next in mapper 

.ranomd is the node.random in mapper 

"""



from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random



class Solution():
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        The function to make the deep copy of the random pointer
        """

        #constraints case
        if not head :
            return None

        if not head.next and not head.random :

            return Node(head.val)

        #make the mapper for new nodes
        mapper = {None:None}

        #ptrs
        temp = head 

        #loop to copy the nodes and store in mapper
        while temp :

            mapper[temp] = Node(temp.val, temp.random)

            temp = temp.next

        #assign the next and values in the prev node

        #new head 
        temp = head
        
        dummy = mapper[head]

        #loop over the nodes 
        while temp :

            mapper[temp].next = mapper[temp.next]
            
            mapper[temp].random = mapper[temp.random]
            
            temp = temp.next

        return dummy




        