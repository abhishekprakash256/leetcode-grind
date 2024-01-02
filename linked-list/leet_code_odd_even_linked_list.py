"""
Make the reaggrangement in the odd evenb linked list 
"""
import linked_list


class Solution():

    def oddEvenList(self,head):
        """
        The function to make the odd and even linked list 
        """

        #make a dummy node
        dummy = linked_list.Node(head.val)
        dummy_head = dummy

        #make the iter pointers 
        temp = head 
        count = 1 

        #start the loop for odd condition  
        while temp and temp.next:

            if count % 2 == 0 : 
                temp = temp.next 
            
            else:
                dummy.next = temp 
                dummy = dummy.next 
                temp = temp.next

            count +=1
        #start the loop for even condition 
        temp = head 
        count = 1

        while temp and temp.next: 

            if count % 2 == 0 :
                dummy = temp.next 
                dummy = dummy.next
                temp = temp.next 

            else:
                temp = temp.next 

            count +=1

        return dummy_head


if __name__ == "__main__":

    sol = Solution()
    helpFun = linked_list.Helper()

    helpFun.printList(linked_list.head)

    res = sol.oddEvenList(linked_list.head)

    helpFun.printList(res)

