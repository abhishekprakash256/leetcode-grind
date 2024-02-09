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