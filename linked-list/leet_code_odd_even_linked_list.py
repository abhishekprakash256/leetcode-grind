"""
Make the reaggrangement in the odd evenb linked list 
"""
import linked_list


class Solution():

    def oddEvenList_incorrect(self,head):
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

    #correct code 
    def oddEvenList(self, head):
        if not head or not head.next:
            return head
        
        odd_head = odd = head
        even_head = even = head.next
        
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        
        odd.next = even_head
        
        return odd_head


if __name__ == "__main__":

    sol = Solution()
    helpFun = linked_list.Helper()

    helpFun.printList(linked_list.head)

    res = sol.oddEvenList(linked_list.head)

    helpFun.printList(res)

