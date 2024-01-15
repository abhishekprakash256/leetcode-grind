"""
convert sorted array into the binary tree

"""

#test cases
inp1 = [-10,-3,0,5,9]
inp2 = [-3,-2,0,4,7]
inp3 = [-2,-2,0,6,6]



class Solution():

	def helper(self,l,r,nums):
		"""
		The helper function to make the base tree

		"""
		#base case for eliminaton
		if l > r:
			return None 

		#find the mid point 
		m = (l+r)//2

		#find the mid node
		node = TreeNode(nums[m])

		#make the node connection
		node.left = self.helper(l,m-1,nums)
		node.right = self.helper(m+1,r,nums)

		return node



	def sortedArrayToBST(self, nums):
		"""
		The fuction to convert the sorted array to tree
		"""

		return self.helper(0,len(nums) -1,nums)



class Solution2(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        mid = len(nums) // 2

        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root

if __name__ == "__main__":

	sol = Solution()
