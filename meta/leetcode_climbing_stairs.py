"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 
"""

"""
Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Constraints:

1 <= n <= 45

"""

"""
using dp -- 

make dp array of num of length n

dp = [0] * (len(nums)+1)

dp[0] = 0 
dp[1] = 1
dp[2] = 2





"""

class Solution:
    """
    passses leetcode
    """
    def climbStairs(self, n: int) -> int:
        """
        The function to find the number of stairs
        """

        #constraint case 

        #1 step
        if n == 1 :

            return 1

        #2 step
        if n == 2 :

            return 2

        #make the dp array 
        dp = [0] * n

        #set the value
        dp[0] = 1
        dp[1] = 2

        for i in range(2,n) :

            dp[i] = dp[i-1] + dp[i-2]


        return dp[-1]

