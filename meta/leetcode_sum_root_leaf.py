"""
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.
"""


"""
Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.



Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.


"""

"""

approach -- 

calculate the height to get the number of zeros on top -- 

dfs approach -- 

make a string and add the number from one till last then convert to string and add 

if hit root add the value in the blank 


"""


class Solution_slow:
    """
    passes leetcode but slow
    """

    def __init__(self):

        self.result = 0 


    def helper_dfs(self,node,curr_val):
        """
        The helper function to add the curr val
        """

        #base case 
        if not node:

            return

        # Append the current node's value to the path sum
        curr_val += str(node.val)

        if not node.left and not node.right:

            self.result += int(curr_val)

            return

        #make the traversal 
        self.helper_dfs(node.left, curr_val )
        self.helper_dfs(node.right , curr_val )





    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        The function to find the sum of the tree as numbers
        """

        #constraint case 

        #no node
        if not root :
            return 0

        #have node left and right null
        if not root.left and not root.right :

            return root.val

        curr_val = ""

        self.helper_dfs(root,curr_val)

        return self.result





class Solution:
    """
    passes leetcode faster solution
    """

    def helper_dfs(self,node,curr_val):
        """
        The helper function to add the curr val
        """

        #base case 
        if not node:

            return 0 

        # Append the current node's value to the path sum
        curr_val = curr_val*10 + node.val

        if not node.left and not node.right:

            return curr_val


        left = self.helper_dfs(node.left , curr_val)
        right = self.helper_dfs(node.right, curr_val )

        return left + right



    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        The function to find the sum of the tree as numbers
        """

        #constraint case 

        #no node
        if not root :
            return 0

        #have node left and right null
        if not root.left and not root.right :

            return root.val

        curr_val = 0

        return self.helper_dfs(root,curr_val)

