"""
The function to find the cousions of the tree

corresponding to the values x and y in the tree are cousins, or false otherwise.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.
"""


"""


Input: root = [1,2,3,4], x = 4, y = 3
Output: false

Example 2:
Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true

Example 3:
Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false

 

Constraints:

The number of nodes in the tree is in the range [2, 100].
1 <= Node.val <= 100
Each node has a unique value.
x != y
x and y are exist in the tree.


"""


"""
approach -- 

we need level parent node dfs can give height :

the helper_dfs can have depth , and also the parent node then match 


check if the value match , 
then check the level match 
then check if parent differnet 
	return true

else:

	return False

how to check node parent ? 

i can do two dfs one to check val 
next to check the level if True 

then check the parent ? 

I have level information and value can match


Constraints:

The number of nodes in the tree is in the range [2, 100].
1 <= Node.val <= 100
Each node has a unique value.
x != y
x and y are exist in the tree.


"""

class Solution_wrong():

	def level_fun(self,node):
		"""

		"""
		pass

	def helper_dfs(self,node,level):
		"""
		The function to find the value and match them
		"""

		#base case
		if not node:

			return False

		#if equal value found 
		if node.val == self.x or node.val == self.y:

			return True

		#add the level up
		level += 1

		#make the left and right recusive call
		left = self.helper_dfs(node.left)
		right = self.helper_dfs(node.right)

		#make the equal case 
		if left == right :




	def isCousins(self,root,x,y):
		"""
		The function to find cousion are equal

		"""
		self.x = x
		self.y = y


		#constraints case 
		if not node :

			return False

		if not root.left and not root.right :

			return False

		#make the recursive calls
		return self.helper_dfs(root,1)






class Solution_wrong2:
	def helper_dfs(self, node, parent, x, y, level):
		"""
		DFS helper function to find the level and parent of nodes x and y.
		"""

		#not node 
		if not node:
			return None, None

		#node val is equal
		if node.val == x:
			return (parent, level)

		#node val is equal
		if node.val == y:
			return (parent, level)
		
		# Search left and right subtrees
		left = self.helper_dfs(node.left, node, x, y, level + 1)
		right = self.helper_dfs(node.right, node, x, y, level + 1)

		# Combine results
		if left[0] and right[0]:  # Both found
			return left, right

		#if left is none and right is none
		return left if left[0] else right


	def isCousins(self, root, x, y):
		"""
		Determines if two nodes are cousins in a binary tree.
		"""
		if not root:
			return False

		# Find the parent and level of both x and y
		x_info, y_info = self.helper_dfs(root, None, x, y, 0)

		# Check if x and y are cousins
		if x_info and y_info:

			return x_info[1] == y_info[1] and x_info[0] != y_info[0]  # Same level, different parents

		return False








class Solution:

    def helper_dfs(self, parent, level):
        """
        The helper function to check for cousin nodes and return
        information about x and y's parent and levels.
        """

        # Base case: if the node is None, return (False, -1)
        if not parent:
            return (False, -1)

        # Check if x or y are direct children of the current node
        is_x_child = parent.left and parent.left.val == self.x
        is_y_child = parent.left and parent.left.val == self.y
        is_x_child = is_x_child or (parent.right and parent.right.val == self.x)
        is_y_child = is_y_child or (parent.right and parent.right.val == self.y)

        # If either x or y is found as a child, return (parent, level + 1)
        if is_x_child or is_y_child:
            return (parent, level + 1)

        # Recursive calls to left and right subtrees
        left = self.helper_dfs(parent.left, level + 1)
        right = self.helper_dfs(parent.right, level + 1)

        # If both nodes are found, check if they are cousins
        if left[0] and right[0]:
            if left[0] != right[0] and left[1] == right[1]:
                return (True, level)  # Cousins found
            else:
                return (False, -1)  # Not cousins

        # Propagate valid results upwards
        return left if left[0] else right

    def isCousins(self, root, x, y):
        """
        Determine if the nodes x and y are cousins.
        """
        self.x = x
        self.y = y

        # Constraints: If the tree is empty or has no children, return False
        if not root or (not root.left and not root.right):
            return False

        # Check for cousins using DFS
        result = self.helper_dfs(root, 0)

        # Return True only if cousins are found
        return result[0] == True














































