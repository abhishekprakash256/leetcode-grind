"""
Given the root of a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.

"""


"""
Input: root = [1,2,3,null,5,null,4]

Output: [1,3,4]


Input: root = [1,2,3,4,null,null,null,5]

Output: [1,3,4,5]


Input: root = [1,null,3]

Output: [1,3]

Example 4:

Input: root = []

Output: []


"""


"""


approach -- 

using bfs 

[1,2,3,5,4]

add the null nodes 

also make the node with 2 intevral and have last element


"""

class Node:

	def __init__(self,val = None, left = None, right = None , next = None):

		self.val = val
		self.left = left
		self.right = right
		self.next = next



#make node 

root = Node(1)
node1 = Node(2)
node2 = Node(3)
node3 = Node(4)
node4 = Node(5)
node5 = Node(7)


#connect the trees

root.left = node1
root.right = node2
node1.left = node3
node1.right = node4
node2.right = node5



class Solution():

    def bfs(self,root):
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

            node = queue.pop(0)
            
            if node : 

                res_lst.append(node.val)

                queue.append(node.left)
    
                queue.append(node.right)

        return res_lst
            



sol = Solution()
print(sol.bfs(root))







