"""

Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

"""

"""

Input: root = [4,2,6,1,3]
Output: 1

Example 2:

Input: root = [1,0,48,null,null,12,49]
Output: 1
"""


"""
using a dfs solution 

calc the abs diff 

start with +inf

update if the value is less

"""

class Node:

	def __init__(self,val = None, left = None, right = None , next = None):

		self.val = val
		self.left = left
		self.right = right
		self.next = next



#make node 

root = Node(1)
node1 = Node(2)
node2 = Node(3)
node3 = Node(4)
node4 = Node(5)
node5 = Node(7)


#connect the trees

root.left = node1
root.right = node2
node1.left = node3
node1.right = node4
node2.right = node5





	





class Solution():


	def dfs_tree(self,node):
		"""
		To dfs traverse the tree
		""" 

		if node:

			self.res_lst.append(node.val)
			

			self.dfs_tree(node.left)

			self.dfs_tree(node.right)


	def getMinimumDifference(self, root) -> int:
		"""
		The function to find the minimum diffrence of the node
		passes leetcode
		"""

		#make the list
		self.res_lst = []

		#make the initial value
		min_val = float("inf")

		#call the dfs function
		self.dfs_tree(root)

		#sort the res list
		self.res_lst.sort()


		for i in range(1,len(self.res_lst)):

			min_val = min(min_val,abs(self.res_lst[i] - self.res_lst[i-1]))


		return min_val









if __name__ == '__main__':
	treehelper = Solution()
	print(treehelper.dfs_tree(root))












		