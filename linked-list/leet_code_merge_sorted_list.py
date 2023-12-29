"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""
import linked_list

class Solution:
    def mergeTwoLists(self, head, head2):
        """
        The function to merge the two linked list that are sorted
        """

        temp, temp2 = head, head2

        while temp:

            print(temp.val)
            temp = temp.next
        

    




if __name__ == "__main__":

    sol = Solution()

    sol.mergeTwoLists(linked_list.head,2)


