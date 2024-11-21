"""
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
"""


"""

Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.





Input: root = []
Output: []

"""

"""
approach -- 

bfs traversal 

with each level make it point to right and level ends point to null 

queue is used in bfs 


"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        #base case 
        if not root :

          return None



        #make the queue
        queue = [root]

        #make the res lst 
        res_lst = []


        while queue :

          temp_lst = []

          for _ in range(len(queue)):

            temp_node = queue.pop(0)

            if temp_node:

              temp_lst.append(temp_node)

              queue.append(temp_node.left)

              queue.append(temp_node.right)

          res_lst.append(temp_lst)


        #connect the nodes 
        for nodes in res_lst : 

            for i in range(len(nodes)-1) :

                nodes[i].next = nodes[i+1]

            nodes[len(nodes)-1].next = None





