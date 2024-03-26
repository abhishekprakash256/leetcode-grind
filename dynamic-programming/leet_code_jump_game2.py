"""
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

"""

#test cases

nums = [2,3,1,1,4]
out = True

nums2 = [3,2,1,0,4]
out2 = False

class Solution():
    def canJump(self,nums):
        """
        Find the jump is possible or not 
        """

        gas = 0 

        for n in nums:

            if gas < 0:
                return False
            
            elif n > gas :
                gas = n 

            gas -=1
        
        return True




sol = Solution()
res = sol.canJump(nums2)

print(res)