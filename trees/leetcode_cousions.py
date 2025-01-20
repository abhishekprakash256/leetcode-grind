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

base case 

if value equal then we match depth and paent match

Constraints:

The number of nodes in the tree is in the range [2, 100].
1 <= Node.val <= 100
Each node has a unique value.
x != y
x and y are exist in the tree.


"""

class Solution():

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
