"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

u can take one steps or two steps
"""

class Solution():

    #----------recursive approach -----------------

    #the time exceeds as the process is slow ----------------
    def climbStairs_slow(self,n):
        """
        The function to find the number of steps needed to climb
        """

        if n == 1 :
            return 1
        
        if n == 2 :
            return 2
        
        return self.climbStairs_slow(n-1) + self.climbStairs_slow(n-2)


    def climbStairs(self,n):
        """
        The function to find the number of the steps required
        """

        #base case 
        if n <= 1:
            return n 
        
        #make the array 
        dp = [0] * (n+1)
        print(dp)
        dp[0]=1
        dp[1]=1

        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
            print(dp[i])
        
        return dp[n]


if __name__ == "__main__":

    sol = Solution()

    res = sol.climbStairs(5)

    print(res)