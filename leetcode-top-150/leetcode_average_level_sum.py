"""
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.
"""


"""

Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5,
 and on level 2 is 11.
Hence return [3, 14.5, 11].
Example 2:


Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]

"""


class Solution():

    def averageOfLevels(self,root):
        """
        The function to do the bfs of the tree
        """

        #base case 
        if not root : 
            return []


        #queue 
        queue = [root]
        res_lst = []

        #start the loop
        while queue :

            level_size = len(queue)
            temp_sum = 0 

            for i in range(level_size):
                 
                node = queue.pop(0)

                temp_sum += node.val
                    
                if node.left : 
                     queue.append(node.left)
                    
                if node.right:
                     queue.append(node.right)

            res_lst.append(temp_sum / level_size)

        return res_lst