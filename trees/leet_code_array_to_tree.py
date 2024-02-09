"""
convert the nums array to binary tree
the nums of array is ascendding order

make a height balanced tree

height of both side is not much diffrence than 1 


"""


"""
Algo ----

nums = [] - is a lst

#contraint case 

if len(nums) == 1:
	return [1]


node = TreeNode(nums[0])
half_tree_len = len(nums) // 2
count = 1
r = 1



while r < len(nums):
	
	temp_node = TreeNode(nums[r])
	if nums[r - 1] < nums[r]:
		temp_node.left = node
		count +=1 

	else:
		temp_node.right = node
		count +=1

	node = temp_node




"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#code is incorrect 
class Solution():

	def sortedArrayToBST(self,nums):
		"""
		The function to make the tree
		"""
		#base case
		if len(nums) == 1:
			node = TreeNode(nums[0])
			return node

		
		#variable initialization
		r = 1
		length = len(nums)
		temp_node = TreeNode(nums[0])

		while r <= (length // 2):

			new_node = TreeNode(nums[r])

			#codn checkig 
			if nums[r - 1] < nums[r]:
				new_node.left = temp_node

			else:
				new_node.right = temp_node

			temp_node = new_node
			r+=1
		
		#assign head
		head = temp_node

		while r < length:

			new_node = TreeNode(nums[r])
			#condn checking
			if nums[r-1] < nums[r]:
				temp_node.right = new_node
			
			else:
				temp_node.left = new_node
			
			temp_node = new_node
			r+=1
		
		return head




