"""
make the maximum profit from selling the stocks 
"""

prices = [7,1,5,3,6,4]
out = 5

prices2 =  [7,6,4,3,1]
out2 = 0 




"""


algo --- 

order is imp


l = 0
r = l+1 

scan the array 

max_profit = 0 

while r < len(prices):
    
    if prices[l] < prices[r]:

        profit = prices[r] - prices[l]
        max_profit = max(profit,max_profit)
        l = r 

    else:
        r +=1

return max_profit

"""


class Solution():

    def maxProfit(self,prices):
        """
        The function to find the max value by selling the stocks
    
        """
        max_profit = 0 
        l = 0 
        r = l + 1

        while r < len(prices):

            if prices[l] < prices[r]:

                profit = prices[r] - prices[l]
                max_profit = max(profit,max_profit)

            else:
                l = r

            r += 1

        return max_profit




if __name__ == '__main__':
    sol = Solution()

    res= sol.maxProfit(prices)

    print(res)












