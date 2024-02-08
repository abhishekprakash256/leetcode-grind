"""
make the append of the bfs node in the list as per order traversal 
"""

"""

Algo -

queue = []
queue.pop(0)

iteration

#base case 
if not node:
	return None

if node.next is None and node.next is None:
	return None 


res = []
queue.append(node.val)


while q:

	level = []
	qlen = len(qlen)

	for i in range(qlen):

		node = q.pop(0)
		
		if node:

			level.append(node.left)
			level.append(ndoe.right)
	
	if level:
		res.append(level)
	
return res



"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#correct soln ------------
class Solution:
    def levelOrder(self, node: Optional[TreeNode]) -> List[List[int]]:
        """
        The bfs iterative approach
        """
        #base case 
        if not node:
            return []
        
        #result list
        res = []
        queue = []
        queue.append(node)
        
        while queue:
            
            qlen = len(queue)
            level = []
            
            for i in range(qlen):
                
                node = queue.pop(0)
                
                if node:
                    
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                
            if level:
                res.append(level)
                    
        return res