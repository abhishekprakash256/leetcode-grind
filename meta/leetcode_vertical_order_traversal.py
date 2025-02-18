"""
Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be at positions
 (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each 
column index starting from the leftmost column and ending on the rightmost column.
 There may be multiple nodes in the same row and same column. In such a case, sort 
 these nodes by their values.

Return the vertical order traversal of the binary tree.

"""

"""
Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation:
Column -1: Only node 9 is in this column.
Column 0: Nodes 3 and 15 are in this column in that order from top to bottom.
Column 1: Only node 20 is in this column.
Column 2: Only node 7 is in this column.
Example 2:

Input: root = [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
Column -2: Only node 4 is in this column.
Column -1: Only node 2 is in this column.
Column 0: Nodes 1, 5, and 6 are in this column.
          1 is at the top, so it comes first.
          5 and 6 are at the same position (2, 0), so we order them by their value, 5 before 6.
Column 1: Only node 3 is in this column.
Column 2: Only node 7 is in this column.
Example 3:

"""

"""

approach -- 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 100

#constaraints case

if not node.left and not node.right :

    return [node.val]


hybrid mapping --

we do a dfs traversal and get the height data in nodes hybrid list 

we can do a bfs traveal and get a col cooredinate 

combine both and make the last list



"""

from collections import deque

class Solution:

    def __init__(self):

        self.dfs_list = []
        self.bfs_list = []
        self.result = []


    def dfs_traversal(self,node,row):
        """
        The function to find the dfs traversal
        """
        
        #base case 
        if not node :

            return

        left = self.dfs_traversal(node.left, row + 1)
        right = self.dfs_traversal(node.right , row + 1 )

        self.dfs_list.append([node.val,row])


    def bfs_traversal(self,node):
        """
        The funciton to make the bfs traversal list
        """

        #add the node 
        queue = deque([(node, 0)])

        #make the iter 
        while queue :

            temp_node , col  = queue.popleft()

            self.bfs_list.append([temp_node.val, col])

            if temp_node.left :

                queue.append((temp_node.left, col - 1 ))

            if temp_node.right :

                queue.append((temp_node.right, col + 1))




    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        The function to make the vertical traversal possible 
        """

        #constraints case 
        if not root.left and not root.right :

            return[root.val]

        #make the traversal
        row = 0 
        self.dfs_traversal(root, row ) 

        #make the bfs traversal
        self.bfs_traversal(root) 

        self.bfs_list = sorted(self.bfs_list, key=lambda x: x[1])


        for node_list in self.bfs_list :

            temp_lst = []

            for val in node_list :

                temp_lst.append(val)

            self.result.append(temp_lst)

        return self.result













        