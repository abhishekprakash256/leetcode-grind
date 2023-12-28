"""
The code to delete the node in linked list 
"""

#import the linked list nodes
import linked_list



class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        temp = linked_list.head

        while True:

            if temp.next is None:
                break

            #break the node
            if temp.next.val == node :
                break_node = temp.next
                temp.next = temp.next.next
                break_node.next = None
                

            temp = temp.next


    def printTree(self,head):
        """
        The function to print the tree 
        """
        temp = head

        while True:

            print(temp.val)

            if temp.next is None:
                break
        
            temp = temp.next
        
            




if __name__ == "__main__":

    sol = Solution()

    tree_print = sol.printTree(linked_list.head)

    res = sol.deleteNode(2)

    tree_print2 = sol.printTree(linked_list.head)


    print(res) 






        

