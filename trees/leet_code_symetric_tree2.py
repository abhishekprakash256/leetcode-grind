"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

left  == right 
and right == left

constraint has one node as well 
"""



"""
algo -- 

recursive algorithm 
handle None values 

compare the halves 

compare the two values on both the ends 

def helper():

	return node.val


def checkSymetry(node.left,node.right):

	left_val = self.helper(node.left) if node.left else None 
	right_val = self.helper(node.right) if node.right else None

	if left_val == right_val : 
		return self.checkSymetry(node.left,node.right) and self.checkSymetry(node.left,node.right)

	else:
		return False



def isSymetric(node):
	#base case 
	if node.left is None and node.right is None:
		return True

	return self.checkSymetry(node.left,node.right)



"""
#incoreect sol ===============
class Solution():
	def helper(self,node):

		#base case
		if not node:
			return None
		
		return node.val

	def checkSymetry(self, nodel, noder):

		#base condn
		if not nodel and not noder:
			return True
		
		if not nodel or not noder:
			return False
		
		left_val = self.helper(nodel) if nodel else None
		right_val = self.helper(noder) if noder else None
		
		return left_val == right_val and self.checkSymetry(nodel.left,nodel.right) and self.checkSymetry(noder.left,noder.right)	

	

	def isSymmetric(self, node: Optional[TreeNode]) -> bool:
		"""
		The main recursive function
		"""
		#base case 
		if node.left is None and node.right is None:
			return True
		
		return self.checkSymetry(node.left,node.right)


if __name__ == "__main__":

	sol = Solution()
