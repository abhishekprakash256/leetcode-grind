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


height is imp 

we get number of tens 


we case use a string and typoe cast to the 


aporoach -- 

dfs but adding values 
so rempty string and carry the vaues freom behind 
res_lst to add all the values 

type cast to all values to int 

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



class Solution:
    def __init__(self):
        self.res_lst = []  # To store all root-to-leaf paths

    def helper(self, node, temp_str):
        """
        Helper function to recursively traverse the tree
        and collect root-to-leaf paths.
        """
        if not node:
            return

        # Append the current node value to the path string
        temp_str += str(node.val)

        # If the node is a leaf, append the path to res_lst
        if not node.left and not node.right:
            self.res_lst.append(temp_str)
        else:
            # Recur for left and right subtrees
            self.helper(node.left, temp_str)
            self.helper(node.right, temp_str)

    def sumNumbers(self, root):
        """
        Function to collect all root-to-leaf paths as strings.
        """
        if not root:
            return []  # Return an empty list if the tree is empty

        # Clear previous results and start the DFS traversal
        self.res_lst = []
        self.helper(root, "")

        for i in range(len(self.res_lst)):

            self.res_lst[i] = int(self.res_lst[i])
        



        return sum(self.res_lst)





if __name__ == '__main__':
    sol = Solution()
    print(sol.dfs_carry(root))
