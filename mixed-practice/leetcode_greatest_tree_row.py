"""
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

"""

"""
approach -- 

use the bfs traversal and iterarte throgh all the values and append the max value

and reset the max value as per level 

constarints the max value can be -ve as well 

so put max as float("-inf")

if not node :

    return []


if root.left is None and root.right is None :

    return [root.val]


"""

from collections import deque


class Solution():

    def __init__(self):

        self.result = []


    def largestValues(self,root):
        """
        The function to return the largest value per row 
        """

        #constarinst case 

        #no node
        if not root :

            return []

        #one node 
        if root.left is None and root.right is None :

            return [root.val]


        #make the queue and add the first val
        q = deque()
        q.append(root)

        #start the iteration

        while q :

            max_val = float("-inf")
            
            #get the length of the queue
            length = len(q)

            for _ in range(length) :

                #pop the node 
                temp_node = q.popleft()

                max_val = max(max_val,temp_node.val)

                if temp_node.left :

                    q.append(temp_node.left)

                if temp_node.right :

                    q.append(temp_node.right)

                
            self.result.append(max_val)

        return self.result


                

                


