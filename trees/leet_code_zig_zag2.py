"""
Make the zig zag level order traversal of the code  
"""


# Example binary tree
#          1
#        /   \
#       2     3
#      / \   / \
#     4   5 6   7
class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

		
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)


#-------not correct code ------------------------------------

class Solution():

    def zigzagLevelOrder_incorrect(self,node):
        """
        The function to give zig zag order traversal 
        """
        #base case 
        if not node:
            return None

        #initilaize the vars 
        queue = []
        queue.append(node)
        res_lst = []
        flip = True 

        while queue:

            node = queue.pop(0)

            if node:
                res_lst.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)


        return res_lst

    def zigzagLevelOrder(self,node):
        """
        The function to append the nodes in zig zag order in tree
        """


        if not node:
            return None 


        #initilaize the queue
        queue = [node]
        res_lst = []

        while queue:

            level = []

            for i in range(len(queue)):

                node = queue.pop(0)

                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            level = list(reversed(level)) if len(res_lst) % 2 else level[:]

            res_lst.append(level)

        return res_lst




if __name__ == "__main__":

    sol = Solution()
    res = sol.zigzagLevelOrder(root)

    print(res)