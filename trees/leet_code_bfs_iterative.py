"""
bfs traversal of the tree iterative
"""


class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

# Creating nodes
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)



class Solution:
    def bfs_recursive(self, nodes, result=None):
        if result is None:
            result = []

        if not nodes:
            return result

        next_level_nodes = []
        for node in nodes:
            if node:
                result.append(node.val)
                if node.left:
                    next_level_nodes.append(node.left)
                if node.right:
                    next_level_nodes.append(node.right)

        return self.bfs_recursive(next_level_nodes, result)

# Example usage:
# Assuming root_node is the root of the binary tree
solution = Solution()
bfs_values = solution.bfs_recursive([root])
print("BFS traversal:", bfs_values)
