"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 
"""


"""
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:

Input: root = []
Output: []





"""




class Solution:
	def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
		"""
		The zig zag traversal of the node in parallel
		"""

		#base case
		if not root :
			return []


		#make the queue
		queue = [root]

		#make the result list 
		res_lst = []

		flip = True


		while queue : 

			temp_lst = []

			level_size = len(queue)


			for _ in range(level_size) : 

				node = queue.pop(0)

				temp_lst.append(node.val)

				if node.left : 

					queue.append(node.left)


				if node.right : 

					queue.append(node.right)


			if flip :

				res_lst.append(temp_lst)

				flip = False


			else :

				temp_lst.reverse()

				res_lst.append(temp_lst)

				flip = True



		return res_lst





