"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a 
file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another 
computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure 
that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
"""

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


#make the tree 


"""
The tree 

	1
   / \
  2   3
	 / \ 		
	4   5  

"""

root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(5)
root.right.left = TreeNode(4)


#print the tree

def tree_printer(node):

	if node:
		print(node.val)

		tree_printer(node.left)
		tree_printer(node.right)



"""
Capture the null values and do bfs 

we implelnmt bfs using a stack iterative apprach 

cath is to capture the null values 

use a stack last in first out 



"""


#write the BFS algo 

class Solution:
    def bfs_traversal(self, root):
        """
        Perform BFS traversal of the tree
        """
        if not root:
            return []

        queue = [root]
        res = []

        while queue:
            node = queue.pop(0)

            if node:
                res.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append(None)  # Append None for None nodes

        return res


#the main function 
if __name__ == "__main__":

	sol = Solution()

	print(sol.bfs_traversal(root))

	#out = [1,2,3,4,5]
	#expected = [1,2,3,null,null,4,5]



