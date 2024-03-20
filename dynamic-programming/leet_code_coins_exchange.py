"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
"""

nums = [1,2,5]
amount1 = 11
out = 3 

nums2 = [2,1,10]
amount2 = 3
out2 = -1

nums3 = [1]
amount3 = 0 
out3 = 0 


"""
Algo -- 

[1,2,5]
11

5 + 5 + 1 = 11

make a tree for calculation of the change of the items 
till one gives zero 

if greater than the sum gives False out 

run DFS in graph to calculate the least height of the tree


if I do memoization then complexity can be saved 


Algo recursion brute force --- 

#vars 
sum_change = -0 

#base case 
if sum_change == amount:
    return True

elif sum_change > amount:
    return False


#constraints
if amount == 0 :
    return 0    

two functions -----


fun helper
(coin, temp_sum,amount)

#base case 

if temp_sum == amount:
    return True

eilf temp_sum > amount:
    return False


for change in coins:
    temp_sum += chnage
    self.helper(temp_sum,change,coins)


-------------------------------
fun coinChange
(coins,amount)

#contraint
if amount == 0:
    return True

temp_sum = 0 

for coin in coins:
    self.helper(temp_sum,coin,coins)

 

"""

class Solution():


    #correct code, not full code
    def helper(self,coin,temp_sum,amount,coins):
        """
        The helper function to find the value
        """

        #base case 

        if temp_sum == amount:
            return True

        if temp_sum > amount:
            return False


        for change in coins:

            temp_sum += change
            if self.helper(coin,temp_sum,amount,coins):
                return True

        return False



    def coinChange(self,coins,amount):
        """
        The main function to calculate change
        """

        #constarints 
        if amount == 0 :
            return 0

        res = False
        temp_sum = 0


        for coin in coins:
            res = self.helper(coin,temp_sum,amount,coins)
            if res:
                return True

        return res



if __name__ == "__main__":

    sol = Solution()

    result = sol.coinChange(nums2,amount2)

    print(result)










