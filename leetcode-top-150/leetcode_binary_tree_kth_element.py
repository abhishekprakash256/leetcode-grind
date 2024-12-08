"""
Given the root of a binary search tree, 
and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
"""

"""
Input: root = [3,1,4,null,2], k = 1
Output: 1

root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
"""

class Solution(object):
	def kthSmallest(self, root, k):
		"""
		:type root: Optional[TreeNode]
		:type k: int
		:rtype: int
		"""

		#base case 
		if not root : 

			return None


		#make the queue 
		queue = [root]


		#res lst 
		res_lst = []


		while queue : 

			curr_node = queue.pop(0)

			if curr_node :

				res_lst.append(curr_node.val)


			if curr_node.left : 

				queue.append(curr_node.left)


			if curr_node.right : 

				queue.append(curr_node.right)


		res_lst.sort()


		return res_lst[k-1] 
		
