"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 
"""
"""
Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []

Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
 

"""



"""


approach -- 

merge using two list and then merge the third in that and so forth 


one merger function 

get two pointers and merge the list 

the other traverse 


"""

class Solution_wrong():

    def _meger_lists(self,node1,node2) :
        """
        The function to merge the twp lists
        """

        #make ptrs

        temp1 = node1
        temp2 = node2

        #start the iter
        while temp1 and temp2 :

            if temp1.val < temp2.val :

                temp_node = temp1

                temp1.next = temp2

                temp1 = temp_node.next

            else:

                temp_node = temp2

                temp2.next = temp1

                temp2 = temp_node.next

        #merge the left over node 
        if temp2 :

            temp1.next = temp2

        if temp1 :

            temp2.next = temp1


 

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        The function to merge the linked list 
        """

        self.lists = lists

        #constarints case
        if not lists :

            return []

        if len(lists) == 1 and not lists[0]:

            return []


        #start the merger 
        for i in range(1,len(self.lists)) :

            self._meger_lists(self.lists[i-1], self.lists[i])


        return lists





from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    passes leet code
    """
    
    def _merge_list(self, node1: Optional[ListNode], node2: Optional[ListNode]) -> Optional[ListNode]:
        """
        The function to merge two sorted linked lists.
        """

        # If one of the lists is empty, return the other.
        if not node1:
            return node2
        if not node2:
            return node1

        # Dummy node to simplify merging.
        dummy = ListNode(0)
        curr = dummy

        while node1 and node2:
            if node1.val < node2.val:
                curr.next = node1
                node1 = node1.next
            else:
                curr.next = node2
                node2 = node2.next

            curr = curr.next  # Move forward

        # Append the remaining elements.
        curr.next = node1 if node1 else node2

        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Merges k sorted linked lists using a divide-and-conquer approach.
        """

        # Edge case: No lists provided
        if not lists:
            return None

        # Edge case: Only one list
        if len(lists) == 1:
            return lists[0]

        while len(lists) > 1:
            
            merged_lists = []

            # Merge pairs of lists
            for i in range(0, len(lists), 2):
                node1 = lists[i]
                node2 = lists[i+1] if i + 1 < len(lists) else None
                merged_lists.append(self._merge_list(node1, node2))

            lists = merged_lists  # Update lists with merged ones

        return lists[0]












        