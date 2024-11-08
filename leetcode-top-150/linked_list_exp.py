"""
The experimentation for linked list
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



class Solution:
    
    def print_list(self,head):
        """
        To print the list
        """

        curr = head

        while curr:

            print(curr.val)
            curr = curr.next

    def print_list2(self,head):

        curr = head

        while curr != None :

            print(curr.val)
            curr = curr.next
    
    def print_list3(self,head):

        curr = head 

        while curr is not None:

            print(curr.val)
            curr = curr.next



    def print_list4(self,head):

        curr = head 

        while True:

            print(curr.val)
            
            if curr.next:
                curr = curr.next
            
            else:
                break



        


sol = Solution()

print(sol.print_list(head))

print(sol.print_list2(head))

print(sol.print_list3(head))

print(sol.print_list4(head))