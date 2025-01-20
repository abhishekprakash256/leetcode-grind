"""
print the right side view of the tree
"""
"""

approach -- 


using the bfs travearal -- 

left goes first

we use a loop over the lebth of ques and append the last elemnt in the result list



"""


from collections import deque


class TreeNode():
	def __init__(self,val,left = None,right = None):

		self.val = val
		self.left = left
		self.right = right


# Example tree:
#       1
#      / \
#     2   3
#    / \
#   4   5

root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))



class Solution():

	def printSideView(self, node):
		"""
		The function to print the tree side view
		passes leetcode
		"""

		#base case 
		if not node :

			return []

		#make the queue
		queue = deque([node])

		#make the result list
		result = []

		#iterate over the queue
		while queue :

			level_size = len(queue)

			for i in range(len(queue)) :

				temp_node = queue.popleft()

				if i == level_size - 1 :

					result.append(temp_node.val)

				if temp_node.left :

					queue.append(temp_node.left)

				if temp_node.right:

					queue.append(temp_node.right)

		return result


sol = Solution()

print(sol.printSideView(root))





		