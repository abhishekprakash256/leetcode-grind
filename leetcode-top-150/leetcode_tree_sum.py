"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up 
all the values along the path equals targetSum.

A leaf is a node with no children.
"""


"""


Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.



Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There are two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

Example 3:

Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.

"""


"""
approach 

use dfs 

make the sum zero on start 

sum = 0 

carry_sum = 0 





"""




class Solution(object):
	def dfs_sum(self,node,temp_sum):
		"""
		The function to find the sum 

		"""

		if node:

			temp_sum += node.val

			if temp_sum == self.targetSum : 

				return True

			self.dfs_sum(node.left,temp_sum)
			self.dfs_sum(node.right,temp_sum)


		return False




    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """

        self.targetSum = targetSum

        #base case
        if not node and sum == 0 :
        	rerurn True

        if not node and sum != 0 :
        	return False


        #make the sum 
        sum = 0 

       return  self.dfs_sum(sum,root)



