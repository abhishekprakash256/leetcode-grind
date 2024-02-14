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

    def zigzagLevelOrder(self,node):
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

            if flip == True :

                if node:
                    res_lst.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

                flip = False
            
            else:
                if node:
                    res_lst.append(node.val)

                if node.right:
                    queue.append(node.right)
                
                if node.left:
                    queue.append(node.left)
        

        return res_lst


if __name__ == "__main__":

    sol = Solution()
    res = sol.zigzagLevelOrder(root)

    print(res)