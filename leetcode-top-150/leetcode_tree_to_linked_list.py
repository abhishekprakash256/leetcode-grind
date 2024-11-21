"""
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node 
in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.

"""

"""

Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Example 2:

Input: root = []
Output: []

Example 3:

Input: root = [0]
Output: [0]

"""

"""

approach -- 

dfs arpoach 

make node and add to right node 


"""

#make node 

class Node:

	def __init__(self,val = None, left = None, right = None , next = None):

		self.val = val
		self.left = left
		self.right = right
		self.next = next

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



class Solution(object):

	def dfs(self,node,node_lst):
		"""
		The function to perform the dfs 
		"""

		if node:

			node_lst.append(node)

			self.dfs(node.left,node_lst)
			self.dfs(node.right,node_lst)


	def flatten(self, root):
		"""
		:type root: Optional[TreeNode]
		:rtype: None Do not return anything, modify root in-place instead.
		passes leetcode
		"""

		#the base case 

		if not root:
			return None

		node_lst = []

		#make the dfs list 

		self.dfs(root,node_lst)


		#add the node like a list 
		
		print(node_lst)

		for i in range(len(node_lst) - 1 ) :

			node_lst[i].right = node_lst[i+1]
			node_lst[i].left = None

			print(i)

		node_lst[i+1].right = None





if __name__ == '__main__':
	sol = Solution()

	print(sol.flatten(root))

